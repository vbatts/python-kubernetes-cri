#!/usr/bin/env python

import grpc
import kubernetes.cri.api_pb2 as pb
import kubernetes.cri.api_pb2_grpc as api

sock = 'unix:/var/run/crio/crio.sock'
channel = grpc.insecure_channel(sock)
image_stub = api.ImageServiceStub(channel)
runtime_stub = api.RuntimeServiceStub(channel)

vers = runtime_stub.Version(pb.VersionRequest())
print(vers)

list_images_response = image_stub.ListImages(pb.ListImagesRequest())
print("found {} images".format(len(list_images_response.images)))
for image in list_images_response.images:
    print("id: {}".format(image.id))
    print("size: {}".format(image.size))
    print("uid: {}".format(image.uid))
    print("username: {}".format(image.username))
    print("repo_tags: {}".format(image.repo_tags))
    print("repo_digests: {}\n".format(image.repo_digests))

list_containers_response = runtime_stub.ListContainers(pb.ListContainersRequest())
print("found {} containers".format(len(list_containers_response.containers)))
for ctr in list_containers_response.containers:
    print(ctr)
