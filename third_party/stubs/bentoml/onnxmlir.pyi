from bentoml.exceptions import MissingDependencyException as MissingDependencyException
from bentoml.service.artifacts import BentoServiceArtifact as BentoServiceArtifact
from bentoml.service.env import BentoServiceEnv as BentoServiceEnv
from typing import Any

class OnnxMlirModelArtifact(BentoServiceArtifact):
    def __init__(self, name) -> None: ...
    def pack(self, onnxmlir_model_so, metadata: Any | None = ...): ...
    def load(self, path): ...
    def set_dependencies(self, env: BentoServiceEnv): ...
    def get(self): ...
    def save(self, dst) -> None: ...