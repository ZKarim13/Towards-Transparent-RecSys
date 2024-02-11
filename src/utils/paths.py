from pathlib import Path

DEFAULT_CONFIG_FILE = "config.yaml"
CONFIG_PATH = "config"
DATASETS_PATH = "datasets"
CACHE_PATH = "cache"
MODELS_PATH = "models"
LOGS_PATH = "logs"
RUNS_PATH = "runs"


class Paths:
    _instance = None

    def __new__(cls, config):
        if cls._instance is None:
            cls._instance = super(Paths, cls).__new__(cls)
        return cls._instance

    def __init__(self, config):
        if not hasattr(self, "_config"):
            self._config = config.get("paths", {})
            self._project_root = Paths.get_project_root()

    @staticmethod
    def get_project_root():
        return Path(__file__).resolve().parent.parent.parent

    @staticmethod
    def get_config_path():
        return Paths.get_project_root() / CONFIG_PATH

    @staticmethod
    def get_config_file():
        return Paths.get_config_path() / DEFAULT_CONFIG_FILE

    def get_datasets_path(self, dataset: str = ""):
        return (
            self._project_root / self._config.get("datasets", DATASETS_PATH) / dataset
        )

    def get_cache_path(self, cache: str = ""):
        return self._project_root / self._config.get("cache", CACHE_PATH) / cache

    def get_models_path(self, model: str = ""):
        return self._project_root / self._config.get("models", MODELS_PATH) / model

    def get_logs_path(self, log: str = ""):
        return self._project_root / self._config.get("logs", LOGS_PATH) / log

    def get_runs_path(self, run: str = ""):
        return self._project_root / self._config.get("runs", RUNS_PATH) / run
