#!/usr/bin/env python

import grpc
import kubernetes.cri.api_pb2 as pb
import kubernetes.cri.api_pb2_grpc as api

from random import randint
from os import getenv

sock = getenv('RUNTIME_SOCK') or 'unix:/var/run/crio/crio.sock'
channel = grpc.insecure_channel(sock)
image_stub = api.ImageServiceStub(channel)
runtime_stub = api.RuntimeServiceStub(channel)

vers = runtime_stub.Version(pb.VersionRequest())
print(vers)

print("pulling docker.io/busybox")
bb_image_spec = pb.ImageSpec(image = 'docker.io/library/busybox')
pull_image_response = image_stub.PullImage(pb.PullImageRequest(
	image = bb_image_spec))
print(pull_image_response.image_ref)

list_images_response = image_stub.ListImages(pb.ListImagesRequest())
print("found {} images".format(len(list_images_response.images)))
for image in list_images_response.images:
	print("id: {}".format(image.id))
	print("size: {}".format(image.size))
	print("uid: {}".format(image.uid))
	print("username: {}".format(image.username))
	print("repo_tags: {}".format(image.repo_tags))
	print("repo_digests: {}\n".format(image.repo_digests))

	# this is redundant, but shows a way to get image status.
	isr = pb.ImageStatusRequest(image=pb.ImageSpec(image=image.id))
	image_status_response = image_stub.ImageStatus(isr)
	print(image_status_response.image)

list_containers_response = runtime_stub.ListContainers(pb.ListContainersRequest())
print("found {} containers".format(len(list_containers_response.containers)))
for ctr in list_containers_response.containers:
	print(ctr)

sandbox_config = pb.PodSandboxConfig(
				metadata = pb.PodSandboxMetadata(
					name = 'python-test-{}'.format(randint(0,1000)),
					namespace = 'test',
					),
				hostname = 'python-test')
# we'll try some error handling
try:
	runpodsandbox_response = runtime_stub.RunPodSandbox(
			pb.RunPodSandboxRequest(
			config = sandbox_config))
except grpc._channel._Rendezvous as e:
	print("failed to run pod sandbox: {}".format(e))
	exit(1)

print('sandbox id: {}'.format(runpodsandbox_response.pod_sandbox_id))

# and create a container in this sandbox
create_container_response = runtime_stub.CreateContainer(
		pb.CreateContainerRequest(
			pod_sandbox_id = runpodsandbox_response.pod_sandbox_id,
			sandbox_config = sandbox_config,
			config = pb.ContainerConfig(
                 metadata = pb.ContainerMetadata(name = sandbox_config.metadata.name),
				image = bb_image_spec,
				command = ['/bin/uptime'],
				)))
