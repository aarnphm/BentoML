from typing import Any

logger: Any
DEBUG_ENV_VAR: str

def expand_env_var(env_var): ...

BENTOML_VERSION: Any
LAST_PYPI_RELEASE_VERSION: Any

def get_local_config_file(): ...
def get_bentoml_deploy_version(bentoml_deploy_version: str): ...
def set_debug_mode(enabled: bool): ...
def get_debug_mode(): ...
def inject_dependencies() -> None: ...