import os

from main import PROJECT_ROOT
from utils.download import download_file
from utils.extract import extract_dataset

from torch.utils.data import Dataset


class BaseDataset(Dataset):

    def __init__(self, config):
        args = config["args"]
        self.dataset_name = args.dataset
        general_config = config.get("general", {})
        dataset_directory = general_config.get("datasets_directory")
        self.datasets_path = os.path.join(PROJECT_ROOT, dataset_directory)
        self.dataset_path = os.path.join(self.datasets_path, self.dataset_name)
        if not self.check_dataset(config):
            self.fetch_dataset(config)

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass

    def check_dataset(self, config) -> bool:
        # TODO: implement the checking here
        # we have all information in the config.
        # the information in the base should be enough.
        if os.path.exists(self.dataset_path):
            print("dataset found")
            return True

        return False

    def fetch_dataset(self, config) -> None:
        general_config = config.get("general", {})
        cache_directory = general_config.get("cache_directory")
        dataset_directory = general_config.get("datasets_directory")
        cache_path = os.path.join(PROJECT_ROOT, cache_directory)
        datasets_path = os.path.join(PROJECT_ROOT, dataset_directory)

        args = config["args"]
        dataset_name = args.dataset

        dataset_config = config.get("datasets").get(dataset_name)
        source = dataset_config.get("source")

        download_path = os.path.join(cache_path, dataset_name)
        download_file(source, download_path)
        extract_dataset(download_path, datasets_path)
