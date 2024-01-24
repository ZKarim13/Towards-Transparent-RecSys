import importlib

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
    def create_dataset(config:dict):
        """Create an instance of the specified dataset class.

        Args:
            dataset (str): The name of the dataset to create.
            config (dict): The configuration containing information about the dataset.

        Returns:
            object: An instance of the specified dataset class.

        Raises:
            ValueError: If the dataset configuration is invalid.
        """
        datasets_config = config.get('datasets', {})
        dataset_config = datasets_config.get(config['args'].dataset, {})
        module_name = dataset_config.get('module')
        class_name = dataset_config.get('class')
        if module_name and class_name:
            module = importlib.import_module(module_name)
            dataset_class = getattr(module, class_name)
        # should of raise some sort of an error indicating that the configuration is wrong.
        return dataset_class(config)





         



