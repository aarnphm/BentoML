from typing import Any

class Status:
    @staticmethod
    def Name(code): ...
    @staticmethod
    def Value(status_name): ...
    @staticmethod
    def OK(message: Any | None = ...): ...
    @staticmethod
    def CANCELLED(message: Any | None = ...): ...
    @staticmethod
    def UNKNOWN(message: Any | None = ...): ...
    @staticmethod
    def INVALID_ARGUMENT(message: Any | None = ...): ...
    @staticmethod
    def DEADLINE_EXCEEDED(message: Any | None = ...): ...
    @staticmethod
    def NOT_FOUND(message: Any | None = ...): ...
    @staticmethod
    def ALREADY_EXISTS(message: Any | None = ...): ...
    @staticmethod
    def PERMISSION_DENIED(message: Any | None = ...): ...
    @staticmethod
    def UNAUTHENTICATED(message: Any | None = ...): ...
    @staticmethod
    def RESOURCE_EXHAUSTED(message: Any | None = ...): ...
    @staticmethod
    def FAILED_RECONDITION(message: Any | None = ...): ...
    @staticmethod
    def ABORTED(message: Any | None = ...): ...
    @staticmethod
    def OUT_OF_RANGE(message: Any | None = ...): ...
    @staticmethod
    def UNIMPLEMENTED(message: Any | None = ...): ...
    @staticmethod
    def INTERNAL(message: Any | None = ...): ...
    @staticmethod
    def UNAVAILABLE(message: Any | None = ...): ...
    @staticmethod
    def DATA_LOSS(message: Any | None = ...): ...
