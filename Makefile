
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
rebuild:
	@echo $(PYTHON)
	$(PYTHON) -m grpc_tools.protoc -I ./vendor/ -I ./protos/ --python_out=. --grpc_python_out=. ./vendor/github.com/gogo/protobuf/gogoproto/gogo.proto
	$(PYTHON) -m grpc_tools.protoc -I ./vendor/ -I ./protos/ --python_out=. --grpc_python_out=. ./protos/api.proto

