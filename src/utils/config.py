import os
import datetime

import yaml

from ..utils.paths import Paths

def load_config():
    """load the default_config_file located in the config_path"""
    config_file = Paths.get_config_file()
    try:
        with open(config_file, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error loading config file {e}")
        raise



def save_config(config):
    paths = Paths(config)
    run = config['args'].name
    if not run:
        current_datetime = datetime.datetime.now()
        run = current_datetime.strftime("run_%Y-%m-%d_%H:%M:%S.yaml")
    else:
        run = run + '.yaml'
    run = paths.get_runs_path(run)
    os.makedirs(os.path.dirname(run), exist_ok=True)
    with open(run, 'w') as file:
        yaml.dump(config, file)
