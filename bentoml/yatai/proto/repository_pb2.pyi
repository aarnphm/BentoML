"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import label_selectors_pb2
import status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BentoUri(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class StorageType(metaclass=_StorageType):
        V = typing.NewType('V', builtins.int)

    UNSET = BentoUri.StorageType.V(0)
    LOCAL = BentoUri.StorageType.V(1)
    S3 = BentoUri.StorageType.V(2)
    GCS = BentoUri.StorageType.V(3)
    AZURE_BLOB_STORAGE = BentoUri.StorageType.V(4)
    HDFS = BentoUri.StorageType.V(5)

    class _StorageType(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[StorageType.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSET = BentoUri.StorageType.V(0)
        LOCAL = BentoUri.StorageType.V(1)
        S3 = BentoUri.StorageType.V(2)
        GCS = BentoUri.StorageType.V(3)
        AZURE_BLOB_STORAGE = BentoUri.StorageType.V(4)
        HDFS = BentoUri.StorageType.V(5)

    TYPE_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    S3_PRESIGNED_URL_FIELD_NUMBER: builtins.int
    GCS_PRESIGNED_URL_FIELD_NUMBER: builtins.int
    type: global___BentoUri.StorageType.V = ...
    uri: typing.Text = ...
    s3_presigned_url: typing.Text = ...
    gcs_presigned_url: typing.Text = ...

    def __init__(self,
        *,
        type : global___BentoUri.StorageType.V = ...,
        uri : typing.Text = ...,
        s3_presigned_url : typing.Text = ...,
        gcs_presigned_url : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"gcs_presigned_url",b"gcs_presigned_url",u"s3_presigned_url",b"s3_presigned_url",u"type",b"type",u"uri",b"uri"]) -> None: ...
global___BentoUri = BentoUri

class BentoServiceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class BentoServiceEnv(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        SETUP_SH_FIELD_NUMBER: builtins.int
        CONDA_ENV_FIELD_NUMBER: builtins.int
        PIP_DEPENDENCIES_FIELD_NUMBER: builtins.int
        PYTHON_VERSION_FIELD_NUMBER: builtins.int
        DOCKER_BASE_IMAGE_FIELD_NUMBER: builtins.int
        PIP_PACKAGES_FIELD_NUMBER: builtins.int
        REQUIREMENTS_TXT_FIELD_NUMBER: builtins.int
        setup_sh: typing.Text = ...
        conda_env: typing.Text = ...
        pip_dependencies: typing.Text = ...
        python_version: typing.Text = ...
        docker_base_image: typing.Text = ...

        @property
        def pip_packages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
        requirements_txt: typing.Text = ...

        def __init__(self,
            *,
            setup_sh : typing.Text = ...,
            conda_env : typing.Text = ...,
            pip_dependencies : typing.Text = ...,
            python_version : typing.Text = ...,
            docker_base_image : typing.Text = ...,
            pip_packages : typing.Optional[typing.Iterable[typing.Text]] = ...,
            requirements_txt : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"conda_env",b"conda_env",u"docker_base_image",b"docker_base_image",u"pip_dependencies",b"pip_dependencies",u"pip_packages",b"pip_packages",u"python_version",b"python_version",u"requirements_txt",b"requirements_txt",u"setup_sh",b"setup_sh"]) -> None: ...

    class BentoArtifact(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        NAME_FIELD_NUMBER: builtins.int
        ARTIFACT_TYPE_FIELD_NUMBER: builtins.int
        METADATA_FIELD_NUMBER: builtins.int
        name: typing.Text = ...
        artifact_type: typing.Text = ...

        @property
        def metadata(self) -> google.protobuf.struct_pb2.Struct: ...

        def __init__(self,
            *,
            name : typing.Text = ...,
            artifact_type : typing.Text = ...,
            metadata : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"artifact_type",b"artifact_type",u"metadata",b"metadata",u"name",b"name"]) -> None: ...

    class BentoServiceApi(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        NAME_FIELD_NUMBER: builtins.int
        INPUT_TYPE_FIELD_NUMBER: builtins.int
        DOCS_FIELD_NUMBER: builtins.int
        INPUT_CONFIG_FIELD_NUMBER: builtins.int
        OUTPUT_CONFIG_FIELD_NUMBER: builtins.int
        OUTPUT_TYPE_FIELD_NUMBER: builtins.int
        MB_MAX_LATENCY_FIELD_NUMBER: builtins.int
        MB_MAX_BATCH_SIZE_FIELD_NUMBER: builtins.int
        BATCH_FIELD_NUMBER: builtins.int
        ROUTE_FIELD_NUMBER: builtins.int
        name: typing.Text = ...
        input_type: typing.Text = ...
        docs: typing.Text = ...
        output_type: typing.Text = ...
        mb_max_latency: builtins.int = ...
        mb_max_batch_size: builtins.int = ...
        batch: builtins.bool = ...
        route: typing.Text = ...

        @property
        def input_config(self) -> google.protobuf.struct_pb2.Struct: ...

        @property
        def output_config(self) -> google.protobuf.struct_pb2.Struct: ...

        def __init__(self,
            *,
            name : typing.Text = ...,
            input_type : typing.Text = ...,
            docs : typing.Text = ...,
            input_config : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
            output_config : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
            output_type : typing.Text = ...,
            mb_max_latency : builtins.int = ...,
            mb_max_batch_size : builtins.int = ...,
            batch : builtins.bool = ...,
            route : typing.Text = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"input_config",b"input_config",u"output_config",b"output_config"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"batch",b"batch",u"docs",b"docs",u"input_config",b"input_config",u"input_type",b"input_type",u"mb_max_batch_size",b"mb_max_batch_size",u"mb_max_latency",b"mb_max_latency",u"name",b"name",u"output_config",b"output_config",u"output_type",b"output_type",u"route",b"route"]) -> None: ...

    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...

        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    ARTIFACTS_FIELD_NUMBER: builtins.int
    APIS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    version: typing.Text = ...

    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...

    @property
    def env(self) -> global___BentoServiceMetadata.BentoServiceEnv: ...

    @property
    def artifacts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BentoServiceMetadata.BentoArtifact]: ...

    @property
    def apis(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BentoServiceMetadata.BentoServiceApi]: ...

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        version : typing.Text = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        env : typing.Optional[global___BentoServiceMetadata.BentoServiceEnv] = ...,
        artifacts : typing.Optional[typing.Iterable[global___BentoServiceMetadata.BentoArtifact]] = ...,
        apis : typing.Optional[typing.Iterable[global___BentoServiceMetadata.BentoServiceApi]] = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"env",b"env"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"apis",b"apis",u"artifacts",b"artifacts",u"created_at",b"created_at",u"env",b"env",u"labels",b"labels",u"name",b"name",u"version",b"version"]) -> None: ...
global___BentoServiceMetadata = BentoServiceMetadata

class Bento(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    BENTO_SERVICE_METADATA_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    version: typing.Text = ...

    @property
    def uri(self) -> global___BentoUri: ...

    @property
    def bento_service_metadata(self) -> global___BentoServiceMetadata: ...

    @property
    def status(self) -> global___UploadStatus: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        version : typing.Text = ...,
        uri : typing.Optional[global___BentoUri] = ...,
        bento_service_metadata : typing.Optional[global___BentoServiceMetadata] = ...,
        status : typing.Optional[global___UploadStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"bento_service_metadata",b"bento_service_metadata",u"status",b"status",u"uri",b"uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_service_metadata",b"bento_service_metadata",u"name",b"name",u"status",b"status",u"uri",b"uri",u"version",b"version"]) -> None: ...
global___Bento = Bento

class AddBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BENTO_NAME_FIELD_NUMBER: builtins.int
    BENTO_VERSION_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    bento_version: typing.Text = ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        bento_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_name",b"bento_name",u"bento_version",b"bento_version"]) -> None: ...
global___AddBentoRequest = AddBentoRequest

class AddBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> status_pb2.Status: ...

    @property
    def uri(self) -> global___BentoUri: ...

    def __init__(self,
        *,
        status : typing.Optional[status_pb2.Status] = ...,
        uri : typing.Optional[global___BentoUri] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status",u"uri",b"uri"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status",u"uri",b"uri"]) -> None: ...
global___AddBentoResponse = AddBentoResponse

class UploadStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Status(metaclass=_Status):
        V = typing.NewType('V', builtins.int)

    UNINITIALIZED = UploadStatus.Status.V(0)
    UPLOADING = UploadStatus.Status.V(1)
    DONE = UploadStatus.Status.V(2)
    ERROR = UploadStatus.Status.V(3)
    TIMEOUT = UploadStatus.Status.V(4)

    class _Status(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Status.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNINITIALIZED = UploadStatus.Status.V(0)
        UPLOADING = UploadStatus.Status.V(1)
        DONE = UploadStatus.Status.V(2)
        ERROR = UploadStatus.Status.V(3)
        TIMEOUT = UploadStatus.Status.V(4)

    STATUS_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    PERCENTAGE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    status: global___UploadStatus.Status.V = ...
    percentage: builtins.int = ...
    error_message: typing.Text = ...

    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...

    def __init__(self,
        *,
        status : global___UploadStatus.Status.V = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        percentage : builtins.int = ...,
        error_message : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"error_message",b"error_message",u"percentage",b"percentage",u"status",b"status",u"updated_at",b"updated_at"]) -> None: ...
global___UploadStatus = UploadStatus

class UpdateBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BENTO_NAME_FIELD_NUMBER: builtins.int
    BENTO_VERSION_FIELD_NUMBER: builtins.int
    UPLOAD_STATUS_FIELD_NUMBER: builtins.int
    SERVICE_METADATA_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    bento_version: typing.Text = ...

    @property
    def upload_status(self) -> global___UploadStatus: ...

    @property
    def service_metadata(self) -> global___BentoServiceMetadata: ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        bento_version : typing.Text = ...,
        upload_status : typing.Optional[global___UploadStatus] = ...,
        service_metadata : typing.Optional[global___BentoServiceMetadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"service_metadata",b"service_metadata",u"upload_status",b"upload_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_name",b"bento_name",u"bento_version",b"bento_version",u"service_metadata",b"service_metadata",u"upload_status",b"upload_status"]) -> None: ...
global___UpdateBentoRequest = UpdateBentoRequest

class UpdateBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> status_pb2.Status: ...

    def __init__(self,
        *,
        status : typing.Optional[status_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> None: ...
global___UpdateBentoResponse = UpdateBentoResponse

class DangerouslyDeleteBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BENTO_NAME_FIELD_NUMBER: builtins.int
    BENTO_VERSION_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    bento_version: typing.Text = ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        bento_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_name",b"bento_name",u"bento_version",b"bento_version"]) -> None: ...
global___DangerouslyDeleteBentoRequest = DangerouslyDeleteBentoRequest

class DangerouslyDeleteBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> status_pb2.Status: ...

    def __init__(self,
        *,
        status : typing.Optional[status_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> None: ...
global___DangerouslyDeleteBentoResponse = DangerouslyDeleteBentoResponse

class GetBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BENTO_NAME_FIELD_NUMBER: builtins.int
    BENTO_VERSION_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    bento_version: typing.Text = ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        bento_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_name",b"bento_name",u"bento_version",b"bento_version"]) -> None: ...
global___GetBentoRequest = GetBentoRequest

class GetBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    BENTO_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> status_pb2.Status: ...

    @property
    def bento(self) -> global___Bento: ...

    def __init__(self,
        *,
        status : typing.Optional[status_pb2.Status] = ...,
        bento : typing.Optional[global___Bento] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"bento",b"bento",u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento",b"bento",u"status",b"status"]) -> None: ...
global___GetBentoResponse = GetBentoResponse

class ListBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class SORTABLE_COLUMN(metaclass=_SORTABLE_COLUMN):
        V = typing.NewType('V', builtins.int)

    created_at = ListBentoRequest.SORTABLE_COLUMN.V(0)
    name = ListBentoRequest.SORTABLE_COLUMN.V(1)

    class _SORTABLE_COLUMN(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[SORTABLE_COLUMN.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        created_at = ListBentoRequest.SORTABLE_COLUMN.V(0)
        name = ListBentoRequest.SORTABLE_COLUMN.V(1)

    BENTO_NAME_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    ASCENDING_ORDER_FIELD_NUMBER: builtins.int
    LABEL_SELECTORS_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    offset: builtins.int = ...
    limit: builtins.int = ...
    order_by: global___ListBentoRequest.SORTABLE_COLUMN.V = ...
    ascending_order: builtins.bool = ...

    @property
    def label_selectors(self) -> label_selectors_pb2.LabelSelectors: ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        offset : builtins.int = ...,
        limit : builtins.int = ...,
        order_by : global___ListBentoRequest.SORTABLE_COLUMN.V = ...,
        ascending_order : builtins.bool = ...,
        label_selectors : typing.Optional[label_selectors_pb2.LabelSelectors] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"label_selectors",b"label_selectors"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"ascending_order",b"ascending_order",u"bento_name",b"bento_name",u"label_selectors",b"label_selectors",u"limit",b"limit",u"offset",b"offset",u"order_by",b"order_by"]) -> None: ...
global___ListBentoRequest = ListBentoRequest

class ListBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    BENTOS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> status_pb2.Status: ...

    @property
    def bentos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Bento]: ...

    def __init__(self,
        *,
        status : typing.Optional[status_pb2.Status] = ...,
        bentos : typing.Optional[typing.Iterable[global___Bento]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bentos",b"bentos",u"status",b"status"]) -> None: ...
global___ListBentoResponse = ListBentoResponse

class ContainerizeBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class BuildArgsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...

        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    BENTO_NAME_FIELD_NUMBER: builtins.int
    BENTO_VERSION_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    BUILD_ARGS_FIELD_NUMBER: builtins.int
    PUSH_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    bento_version: typing.Text = ...
    tag: typing.Text = ...
    push: builtins.bool = ...

    @property
    def build_args(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        bento_version : typing.Text = ...,
        tag : typing.Text = ...,
        build_args : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        push : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_name",b"bento_name",u"bento_version",b"bento_version",u"build_args",b"build_args",u"push",b"push",u"tag",b"tag"]) -> None: ...
global___ContainerizeBentoRequest = ContainerizeBentoRequest

class ContainerizeBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    tag: typing.Text = ...

    @property
    def status(self) -> status_pb2.Status: ...

    def __init__(self,
        *,
        status : typing.Optional[status_pb2.Status] = ...,
        tag : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status",u"tag",b"tag"]) -> None: ...
global___ContainerizeBentoResponse = ContainerizeBentoResponse

class UploadBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BENTO_NAME_FIELD_NUMBER: builtins.int
    BENTO_VERSION_FIELD_NUMBER: builtins.int
    BENTO_BUNDLE_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    bento_version: typing.Text = ...
    bento_bundle: builtins.bytes = ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        bento_version : typing.Text = ...,
        bento_bundle : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_bundle",b"bento_bundle",u"bento_name",b"bento_name",u"bento_version",b"bento_version"]) -> None: ...
global___UploadBentoRequest = UploadBentoRequest

class UploadBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> status_pb2.Status: ...

    def __init__(self,
        *,
        status : typing.Optional[status_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> None: ...
global___UploadBentoResponse = UploadBentoResponse

class DownloadBentoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BENTO_NAME_FIELD_NUMBER: builtins.int
    BENTO_VERSION_FIELD_NUMBER: builtins.int
    bento_name: typing.Text = ...
    bento_version: typing.Text = ...

    def __init__(self,
        *,
        bento_name : typing.Text = ...,
        bento_version : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_name",b"bento_name",u"bento_version",b"bento_version"]) -> None: ...
global___DownloadBentoRequest = DownloadBentoRequest

class DownloadBentoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BENTO_BUNDLE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    bento_bundle: builtins.bytes = ...

    @property
    def status(self) -> status_pb2.Status: ...

    def __init__(self,
        *,
        bento_bundle : builtins.bytes = ...,
        status : typing.Optional[status_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bento_bundle",b"bento_bundle",u"status",b"status"]) -> None: ...
global___DownloadBentoResponse = DownloadBentoResponse
