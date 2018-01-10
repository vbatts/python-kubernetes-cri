#!/usr/bin/env python

from distutils.core import setup

setup(name='kubernetes-cri',
      version='0.1',
      description='python bindings for the Kubernetes Container Runtime Interface (CRI) gRPC',
      author='Vincent Batts',
      author_email='vbatts@hashbangbash.com',
      url='https://github.com/vbatts/python-kubernetes-cri',
      license='MIT',
      py_modules=[
          'api_pb2_grpc',
          'api_pb2',
          'github',
          'github.com',
          'github.com.gogo',
          'github.com.gogo.protobuf',
          'github.com.gogo.protobuf.gogoproto',
          'github.com.gogo.protobuf.gogoproto.gogo_pb2',
          ],
        )
