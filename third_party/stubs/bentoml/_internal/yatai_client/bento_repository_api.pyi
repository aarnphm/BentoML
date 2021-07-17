from bentoml.exceptions import BentoMLException as BentoMLException, BentoMLRpcError as BentoMLRpcError
from bentoml.saved_bundle import load_bento_service_metadata as load_bento_service_metadata, load_from_dir as load_from_dir, safe_retrieve as safe_retrieve, save_to_dir as save_to_dir
from bentoml.service import BentoService as BentoService
from bentoml.utils import is_gcs_url as is_gcs_url, is_s3_url as is_s3_url, resolve_bento_bundle_uri as resolve_bento_bundle_uri, status_pb_to_error_code_and_message as status_pb_to_error_code_and_message
from bentoml.utils.lazy_loader import LazyLoader as LazyLoader
from bentoml.utils.tempdir import TempDirectory as TempDirectory
from bentoml.yatai.client import YataiClient as YataiClient
from bentoml.yatai.client.label_utils import generate_gprc_labels_selector as generate_gprc_labels_selector
from bentoml.yatai.grpc_stream_utils import UploadBentoStreamRequests as UploadBentoStreamRequests
from bentoml.yatai.proto import status_pb2 as status_pb2
from bentoml.yatai.proto.repository_pb2 import AddBentoRequest as AddBentoRequest, Bento as Bento, BentoUri as BentoUri, ContainerizeBentoRequest as ContainerizeBentoRequest, DangerouslyDeleteBentoRequest as DangerouslyDeleteBentoRequest, DownloadBentoRequest as DownloadBentoRequest, GetBentoRequest as GetBentoRequest, ListBentoRequest as ListBentoRequest, UpdateBentoRequest as UpdateBentoRequest, UploadStatus as UploadStatus
from bentoml.yatai.proto.yatai_service_pb2_grpc import YataiStub as YataiStub
from bentoml.yatai.status import Status as Status
from typing import Any, Dict, List, Optional

logger: Any
yatai_proto: Any
DEFAULT_GRPC_REQUEST_TIMEOUT: int

def is_remote_yatai(yatai_service) -> bool: ...

class BentoRepositoryAPIClient:
    yatai_service: Any
    def __init__(self, yatai_service) -> None: ...
    def push(self, bento: str, with_labels: bool = ...) -> BentoUri: ...
    def pull(self, bento: str) -> BentoUri: ...
    def upload(self, bento_service: BentoService, version: str = ..., labels: Dict = ...) -> BentoUri: ...
    def upload_from_dir(self, saved_bento_path: str, labels: Dict = ...) -> BentoUri: ...
    def download_to_directory(self, bento_pb, target_dir: str) -> None: ...
    def get(self, bento: str) -> Bento: ...
    def list(self, bento_name: str = ..., offset: int = ..., limit: int = ..., order_by: str = ..., ascending_order: bool = ..., labels: str = ...) -> List[Bento]: ...
    def delete(self, bento_tag: str = ..., labels: str = ..., bento_name: str = ..., bento_version: str = ..., prune: Optional[bool] = ..., require_confirm: Optional[bool] = ...) -> None: ...
    def containerize(self, bento: str, tag: str, build_args: Dict[str, str] = ..., push: bool = ...) -> str: ...
    def load(self, bento: str) -> BentoService: ...
