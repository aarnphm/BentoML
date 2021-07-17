from bentoml.exceptions import MissingDependencyException as MissingDependencyException
from bentoml.service.artifacts import BentoServiceArtifact as BentoServiceArtifact
from bentoml.service.env import BentoServiceEnv as BentoServiceEnv
from bentoml.utils.tensorflow import cast_tensor_by_spec as cast_tensor_by_spec, get_arg_names as get_arg_names, get_input_signatures as get_input_signatures, get_restored_functions as get_restored_functions, pretty_format_restored_model as pretty_format_restored_model
from typing import Any

logger: Any

class _TensorflowFunctionWrapper:
    origin_func: Any
    arg_names: Any
    arg_specs: Any
    kwarg_specs: Any
    def __init__(self, origin_func, arg_names: Any | None = ..., arg_specs: Any | None = ..., kwarg_specs: Any | None = ...) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __getattr__(self, k): ...
    @classmethod
    def hook_loaded_model(cls, loaded_model) -> None: ...

class TensorflowSavedModelArtifact(BentoServiceArtifact):
    def __init__(self, name) -> None: ...
    def set_dependencies(self, env: BentoServiceEnv): ...
    def pack(self, obj, metadata: Any | None = ..., signatures: Any | None = ..., options: Any | None = ...): ...
    def get(self): ...
    def load(self, path): ...
    def save(self, dst) -> None: ...
    def __del__(self) -> None: ...