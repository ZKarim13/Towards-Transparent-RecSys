from datasets.base_dataset import BaseDataset
import os
import pandas as pd
import torch


class MovielensDataset(BaseDataset):
    def __init__(self, config):
        super().__init__(config)
        # should the reading of the dataset be part of the dataset class?
        # what logic should i put here ??
        # try to have more coner separaiton cause this will get messi very quickly.
        df = pd.read_csv(os.path.join(self.dataset_path, 'ratings.csv'))

        self.user_mapping = {user_id: idx for idx, user_id in enumerate(df['userId'].unique())}
        self.users = torch.tensor(df['userId'].map(self.user_mapping), dtype=torch.int)

        self.movie_mapping = {movie_id: idx for idx, movie_id in enumerate(df['movieId'].unique())}
        self.movies = torch.tensor(df['movieId'].map(self.movie_mapping), dtype=torch.int)

        self.ratings = torch.tensor(df['rating'])


    def __len__(self):
        return len(self.users)

    def __getitem__(self, index):
        return self.users[index], self.movies[index], self.ratings[index]    


    def num_users(self):
        return len(self.user_mapping)

    def num_movies(self):
        return len(self.movie_mapping)