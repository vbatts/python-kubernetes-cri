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
