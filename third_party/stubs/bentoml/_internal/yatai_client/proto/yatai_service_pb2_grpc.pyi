from typing import Any

class YataiStub:
    HealthCheck: Any
    GetYataiServiceVersion: Any
    ApplyDeployment: Any
    DeleteDeployment: Any
    GetDeployment: Any
    DescribeDeployment: Any
    ListDeployments: Any
    AddBento: Any
    UpdateBento: Any
    GetBento: Any
    DangerouslyDeleteBento: Any
    ListBento: Any
    ContainerizeBento: Any
    UploadBento: Any
    DownloadBento: Any
    def __init__(self, channel) -> None: ...

class YataiServicer:
    def HealthCheck(self, request, context) -> None: ...
    def GetYataiServiceVersion(self, request, context) -> None: ...
    def ApplyDeployment(self, request, context) -> None: ...
    def DeleteDeployment(self, request, context) -> None: ...
    def GetDeployment(self, request, context) -> None: ...
    def DescribeDeployment(self, request, context) -> None: ...
    def ListDeployments(self, request, context) -> None: ...
    def AddBento(self, request, context) -> None: ...
    def UpdateBento(self, request, context) -> None: ...
    def GetBento(self, request, context) -> None: ...
    def DangerouslyDeleteBento(self, request, context) -> None: ...
    def ListBento(self, request, context) -> None: ...
    def ContainerizeBento(self, request, context) -> None: ...
    def UploadBento(self, request_iterator, context) -> None: ...
    def DownloadBento(self, request, context) -> None: ...

def add_YataiServicer_to_server(servicer, server) -> None: ...

class Yatai:
    @staticmethod
    def HealthCheck(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def GetYataiServiceVersion(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def ApplyDeployment(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def DeleteDeployment(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def GetDeployment(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def DescribeDeployment(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def ListDeployments(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def AddBento(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def UpdateBento(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def GetBento(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def DangerouslyDeleteBento(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def ListBento(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def ContainerizeBento(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def UploadBento(request_iterator, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
    @staticmethod
    def DownloadBento(request, target, options=..., channel_credentials: Any | None = ..., call_credentials: Any | None = ..., insecure: bool = ..., compression: Any | None = ..., wait_for_ready: Any | None = ..., timeout: Any | None = ..., metadata: Any | None = ...): ...
