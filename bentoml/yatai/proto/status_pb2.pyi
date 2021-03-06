"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Code(metaclass=_Code):
        V = typing.NewType('V', builtins.int)

    OK = Status.Code.V(0)
    CANCELLED = Status.Code.V(1)
    UNKNOWN = Status.Code.V(2)
    INVALID_ARGUMENT = Status.Code.V(3)
    DEADLINE_EXCEEDED = Status.Code.V(4)
    NOT_FOUND = Status.Code.V(5)
    ALREADY_EXISTS = Status.Code.V(6)
    PERMISSION_DENIED = Status.Code.V(7)
    UNAUTHENTICATED = Status.Code.V(16)
    RESOURCE_EXHAUSTED = Status.Code.V(8)
    FAILED_PRECONDITION = Status.Code.V(9)
    ABORTED = Status.Code.V(10)
    OUT_OF_RANGE = Status.Code.V(11)
    UNIMPLEMENTED = Status.Code.V(12)
    INTERNAL = Status.Code.V(13)
    UNAVAILABLE = Status.Code.V(14)
    DATA_LOSS = Status.Code.V(15)
    DO_NOT_USE_RESERVED_FOR_FUTURE_EXPANSION_USE_DEFAULT_IN_SWITCH_INSTEAD_ = Status.Code.V(20)

    class _Code(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Code.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        OK = Status.Code.V(0)
        CANCELLED = Status.Code.V(1)
        UNKNOWN = Status.Code.V(2)
        INVALID_ARGUMENT = Status.Code.V(3)
        DEADLINE_EXCEEDED = Status.Code.V(4)
        NOT_FOUND = Status.Code.V(5)
        ALREADY_EXISTS = Status.Code.V(6)
        PERMISSION_DENIED = Status.Code.V(7)
        UNAUTHENTICATED = Status.Code.V(16)
        RESOURCE_EXHAUSTED = Status.Code.V(8)
        FAILED_PRECONDITION = Status.Code.V(9)
        ABORTED = Status.Code.V(10)
        OUT_OF_RANGE = Status.Code.V(11)
        UNIMPLEMENTED = Status.Code.V(12)
        INTERNAL = Status.Code.V(13)
        UNAVAILABLE = Status.Code.V(14)
        DATA_LOSS = Status.Code.V(15)
        DO_NOT_USE_RESERVED_FOR_FUTURE_EXPANSION_USE_DEFAULT_IN_SWITCH_INSTEAD_ = Status.Code.V(20)

    STATUS_CODE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    status_code: global___Status.Code.V = ...
    error_message: typing.Text = ...

    def __init__(self,
        *,
        status_code : global___Status.Code.V = ...,
        error_message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"error_message",b"error_message",u"status_code",b"status_code"]) -> None: ...
global___Status = Status
