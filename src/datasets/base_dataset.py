from abc import ABC, abstractmethod

class BaseDataset(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, index):
        pass
