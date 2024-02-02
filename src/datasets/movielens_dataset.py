import pandas as pd
import torch

from .base_dataset import BaseDataset


class MovielensDataset(BaseDataset):
    def __init__(self, config):
        super().__init__(config)
        df = pd.read_csv(
            self.paths.get_datasets_path(self.dataset_name) / "ratings.csv"
        )

        self.user_mapping = {
            user_id: idx for idx, user_id in enumerate(df["userId"].unique())
        }
        self.users = torch.tensor(df["userId"].map(self.user_mapping), dtype=torch.int)

        self.movie_mapping = {
            movie_id: idx for idx, movie_id in enumerate(df["movieId"].unique())
        }
        self.movies = torch.tensor(
            df["movieId"].map(self.movie_mapping), dtype=torch.int
        )

        self.ratings = torch.tensor(df["rating"])

    def __len__(self):
        return len(self.users)

    def __getitem__(self, index):
        return self.users[index], self.movies[index], self.ratings[index]

    def num_users(self):
        return len(self.user_mapping)

    def num_movies(self):
        return len(self.movie_mapping)
