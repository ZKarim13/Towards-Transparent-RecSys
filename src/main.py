import os
import argparse
import yaml
from datasets.dataset_factory import DatasetFactory
# later extract thoese from here for better code design also for speed.
from torch.utils.data import DataLoader
import torch
from torch import nn
from models.simple_model import SimpleModel


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


def create_directories(config):
    general_config = config.get('general', {})
    cache_directory = general_config.get('cache_directory')
    dataset_directory = general_config.get('datasets_directory')
    cache_path = os.path.join(PROJECT_ROOT, cache_directory)
    datasets_path = os.path.join(PROJECT_ROOT, dataset_directory)
    os.makedirs(datasets_path, exist_ok=True)
    os.makedirs(cache_path, exist_ok=True)

# extract the training loop from the main file
def train(config):
    dataset = DatasetFactory.create_dataset(config) 
    num_users = dataset.num_users()
    num_movies = dataset.num_movies()
    embedding_size = 64
    model = SimpleModel(num_users, num_movies, embedding_size).to(dtype=torch.float)
    epochs = 30
    data_loader = DataLoader(dataset, batch_size=64)
    
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


    model.train()
    for epoch in range(epochs):
        print(f'Epoch {epoch + 1}----------------------')
        for i, batch in enumerate(data_loader):
            optimizer.zero_grad()
            users, movies, ratings = batch
            ratings = ratings.to(dtype=torch.float)
            prediction = model(users, movies)
            loss = criterion(prediction, ratings)
            loss.backward()
            optimizer.step()
            if (i % 100)== 0:
                print(f'batch {i}/{len(data_loader)} loss : {loss}')


    # save the model after training..



def explain(config):
    print('the "explain" command is not yet implemented.')




def main():

    # Load the configuration
    config = load_config()

    # create necessary directories
    create_directories(config)

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
