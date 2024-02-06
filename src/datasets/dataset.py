import os
from torch.utils.data import Dataset as TDS

from .dataset_factory import DatasetFactory
from ..utils.download import download_file
from ..utils.extract import extract_dataset
from ..utils.paths import Paths

class Dataset(TDS):
    def __init__(self, config):
        self.dataset_name = config["args"].dataset
        self.paths = Paths(config)
        self.config = config.get("datasets").get(self.dataset_name)
        if not self.check_dataset():
            self.fetch_dataset()
        self.dataset = DatasetFactory.create_dataset(config)

    def __len__(self):
        return self.dataset.__len__()

    def __getitem__(self, index):
        return self.dataset.__getitem__(index)

    def check_dataset(self) -> bool:
        dataset_path = self.paths.get_datasets_path(self.dataset_name)
        if os.path.exists(dataset_path):
            print("dataset found")
            return True

        return False

    def fetch_dataset(self) -> None:
        source = self.config.get("source")

        download_path = self.paths.get_cache_path(self.dataset_name)
        dataset_path = self.paths.get_datasets_path()

        download_file(source, download_path)
        extract_dataset(download_path, dataset_path)
