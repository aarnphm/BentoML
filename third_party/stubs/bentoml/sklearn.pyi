from bentoml.exceptions import MissingDependencyException as MissingDependencyException
from bentoml.service.artifacts import BentoServiceArtifact as BentoServiceArtifact
from bentoml.service.env import BentoServiceEnv as BentoServiceEnv
from typing import Any

DEFAULT_PICKLE_EXTENSION: str

class SklearnModelArtifact(BentoServiceArtifact):
    def __init__(self, name) -> None: ...
    def pack(self, sklearn_model, metadata: Any | None = ...): ...
    def load(self, path): ...
    def get(self): ...
    def save(self, dst) -> None: ...
    def set_dependencies(self, env: BentoServiceEnv): ...
