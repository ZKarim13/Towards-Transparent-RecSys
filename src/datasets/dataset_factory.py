import importlib
from ..utils.paths import Paths


class DatasetFactory:
    """Factory class for creating dataset instances.

    This factory is responsible for dynamically creating instances of dataset classes based on
    the provided configuration. Each dataset class should handle specific logic for downloading
    and loading data.

    Attributes:
        None

    Methods:
       create_dataset(dataset, config): Create an instance of the specified dataset class.

    Example:

        # Usage example:
        from datasets.dataset_factory import create_dataset
        dataset_instance = DatasetFactory.create_dataset("movielens", config)

    """

    @staticmethod
    def create_dataset(config: dict):
        """Create an instance of the specified dataset class.

        Args:
            dataset (str): The name of the dataset to create.
            config (dict): The configuration containing information about the dataset.

        Returns:
            object: An instance of the specified dataset class.

        Raises:
            ValueError: If the dataset configuration is invalid.
        """
        dataset = config['args'].dataset
        datasets_config = config.get("datasets", {})
        dataset_config = datasets_config.get(dataset, {})
        module_name = dataset_config.get("module")
        try:
            module = importlib.import_module(module_name)
            dataset_class = module.initialize()
        except Exception as e:
            print(e)
        paths = Paths(config)
        return dataset_class(paths.get_datasets_path(dataset))
