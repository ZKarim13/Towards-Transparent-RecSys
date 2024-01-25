from torch import nn
import torch


class SimpleModel(nn.Module):
    def __init__(self, num_users, num_movies, embedding_size=50):
        super(SimpleModel, self).__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_size, dtype=torch.float)
        self.movie_embedding = nn.Embedding(num_movies, embedding_size, dtype=torch.float)
        self.linear = nn.Linear(embedding_size * 2, 1)

    def forward(self, user_idx, movie_idx):
        user_emb = self.user_embedding(user_idx)
        movie_emb = self.movie_embedding(movie_idx)
        concat_emb = torch.cat([user_emb, movie_emb], dim=1)
        prediction = self.linear(concat_emb)
        return prediction.squeeze()
