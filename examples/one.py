#!/usr/bin/env python

import grpc
import kubernetes.cri.api_pb2_grpc as api

print(api)

channel = grpc.insecure_channel('/var/run/crio/crio.sock')
image_stub = api.ImageServiceStub(channel)
runtime_stub = api.RuntimeServiceStub(channel)

print(image_stub)
print(runtime_stub)
