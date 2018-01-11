#!/usr/bin/env python

from distutils.core import setup

setup(name='kubernetes-cri',
      version='0.1.3',
      description='python bindings for the Kubernetes Container Runtime Interface (CRI) gRPC',
      long_description='''
These bindings use the api.proto from kubernetes, as well as the compiled
protobuf package for gogoproto (`github.com.gogo.protobuf.gogoproto`).
      ''',
      author='Vincent Batts',
      author_email='vbatts@hashbangbash.com',
      url='https://github.com/vbatts/python-kubernetes-cri',
      license='MIT',
      packages=[
          'kubernetes.cri',
          'github',
          'github.com',
          'github.com.gogo',
          'github.com.gogo.protobuf',
          'github.com.gogo.protobuf.gogoproto',
          ],
      package_dir={
          'kubernetes.cri': 'src/kubernetes/cri',
          'github': 'src/github/',
          },
      install_requires=[
          'grpcio-tools',
          ],
        )
