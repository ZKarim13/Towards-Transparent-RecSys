import os

from torch.utils.data import Dataset

from ..utils.download import download_file
from ..utils.extract import extract_dataset
from ..utils.paths import Paths


class BaseDataset(Dataset):

    def __init__(self, config):
        self.dataset_name = config["args"].dataset
        self.config = config.get("datasets").get(self.dataset_name)
        self.paths = Paths(config)

        if not self.check_dataset():
            self.fetch_dataset()

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
