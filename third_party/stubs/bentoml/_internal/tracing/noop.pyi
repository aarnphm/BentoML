from typing import Any

logger: Any

class NoopTracer:
    def __init__(self) -> None: ...
    def span(self, *args, **kwargs) -> None: ...
    def async_span(self, *args, **kwargs) -> None: ...
