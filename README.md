# python-k8s-cri

Python bindings for the kubernetes CRI (container runtime interface) gRPC

__Note:__ This is an early trial and is subject to change

## Install

```shell
pip install kubernetes-cri
```

## Usage

The pydoc of these generated files is terrible, and really requires getting familiar with the transaction between server and client, and then sitting with the api.proto open for review of field names, funcations and returns.

See [the gRPC python tutorial](https://grpc.io/docs/tutorials/basic/python.html) to get a bit more familiar on the approach.

See the [examples/](./examples/) for client usages.

## rebuilding from .proto

Requires `pip install grpcio-tools`.

```shell
make rebuild
```

## api.proto

The version of api.proto used intially is from [kubernetes v1.7.12](https://github.com/kubernetes/kubernetes/blob/v1.7.12/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto).

TODO: automate fetching multiple versions, and have them in independent python package paths

## gogoprotobuf

The vendored protobuf from https://github.com/gogo/protobuf/gogoproto
is commit c0656edd0d9eab7c66d1eb0c568f9039345796f7

TODO: use a tool to automate this vendoring

