import os
import argparse
import yaml
from datasets.dataset_factory import DatasetFactory


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG_FILE = 'config/config.yaml'

def load_config():
    config_file_path = os.path.join(PROJECT_ROOT, DEFAULT_CONFIG_FILE)

    try: 
        with open(config_file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f'Error loading config file {e}')
        raise



# extract the training loop from the main file
def train(config):
    dataset = DatasetFactory.create_dataset(config) 



def explain(config):
    print('the "explain" command is not yet implemented.')




def main():

    # Load the configuration
    config = load_config()

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Commends',
                                       dest='command',
                                       required=True,
                                       )
    
    # train command
    train_parser = subparsers.add_parser('train', help='train a model')
    # train_parser.add_argument('architecture')
    train_parser.add_argument('--dataset',
                              help='dataset that will be used in training',
                              type=str,
                              choices=config.get('datasets').keys(),
                              required=True,
                              )
    train_parser.add_argument('-v',
                              '--verbose',
                              action='store_true'
                              )
    train_parser.set_defaults(func=train)
     
    
    # explain command
    explain_parser = subparsers.add_parser('explain',
                                           help='explain a model', 
                                           epilog='the "explain" command is not yer implemented')
    explain_parser.set_defaults(func=explain)
    
    



    args = parser.parse_args()
    config['args'] = args
    args.func(config)

    ###########################
    for _ in range(5):
        print()
    print(vars(args))



if __name__ == '__main__':
    main()
