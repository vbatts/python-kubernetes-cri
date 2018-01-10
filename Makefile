
PYTHON ?= $(shell command -v python)

.PHONY: clean
clean:
	rm -rf *~


# this may need to have a map of versions of protos to download ... 
# from https://github.com/kubernetes/kubernetes/releases
#
# master: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
#         https://raw.githubusercontent.com/kubernetes/kubernetes/master/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
# 1.9.1: https://github.com/kubernetes/kubernetes/blob/v1.9.1/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
#        https://raw.githubusercontent.com/kubernetes/kubernetes/v1.9.1/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
# 1.8.6: https://github.com/kubernetes/kubernetes/blob/v1.8.6/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
#        https://raw.githubusercontent.com/kubernetes/kubernetes/v1.8.6/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
# 1.7.12: https://github.com/kubernetes/kubernetes/blob/v1.7.12/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
#         https://raw.githubusercontent.com/kubernetes/kubernetes/v1.7.12/pkg/kubelet/apis/cri/v1alpha1/runtime/api.proto
rebuild: src src/github/com/gogo/protobuf/gogoproto/gogo_pb2.py src/kubernetes/cri/api_pb2_grpc.py

src:
	mkdir -p src

src/github/com/gogo/protobuf/gogoproto/gogo_pb2.py: ./vendor/github.com/gogo/protobuf/gogoproto/gogo.proto
	$(PYTHON) -m grpc_tools.protoc -I ./vendor/ -I ./protos/ --python_out=./src/ --grpc_python_out=./src/ ./vendor/github.com/gogo/protobuf/gogoproto/gogo.proto
	rm -rf src/github.com/
	find src/github/ -type d -exec touch "{}/__init__.py" \;

src/kubernetes/cri/api_pb2_grpc.py: protos/kubernetes/cri/api.proto
	mkdir -p src/kubernetes/cri
	$(PYTHON) -m grpc_tools.protoc -I ./vendor/ -I ./protos/ --python_out=./src/ --grpc_python_out=./src/ ./protos/kubernetes/cri/api.proto
	find src/kubernetes/cri/ -type d -exec touch "{}/__init__.py" \;
