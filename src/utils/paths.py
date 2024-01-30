from pathlib import Path

DATASETS_PATH = 'datasets'
CACHE_PATH = 'cache'
MODELS_PATH = 'models'
LOGS_PATH = 'logs'


class Paths:
    _instance = None

    def __new__(cls, config):
        if cls._instance is None:
            cls._instance = super(Paths, cls).__new__(cls)
            cls._instance._config = config.get('paths', {})
            cls._instance._project_root = Path(__file__).resolve().parent.parent.parent
        return cls._instance
    
    def get_project_root(self):
        return self._project_root

    def get_datasets_path(self):
        return self._project_root / self._config.get('datasets', DATASETS_PATH)

    def get_cache_path(self):
        return self._project_root / self._config.get('cache', CACHE_PATH)

    def get_models_path(self):
        return self._project_root / self._config.get('models', MODELS_PATH)

    def get_logs_path(self):
        return self._project_root / self._config.get('logs', LOGS_PATH)
