import torch
from torch import nn
from torch.utils.data import DataLoader

from .models.simple_model import SimpleModel
from .datasets.dataset import Dataset



class Gym():
    def __init__(self, config):
        self.dataset = Dataset(config)
        num_users = self.dataset.dataset.num_users()
        num_movies = self.dataset.dataset.num_movies()
        embedding_size = 64
        #self.model = Model(config)
        self.model = SimpleModel(num_users, num_movies, embedding_size).to(dtype=torch.float)

    def train(self):
        epochs = 30
        data_loader = DataLoader(self.dataset, batch_size=64)
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)

        self.model.train()
        for epoch in range(epochs):
            print(f"Epoch {epoch + 1}----------------------")
            for i, batch in enumerate(data_loader):
                optimizer.zero_grad()
                users, movies, ratings = batch
                ratings = ratings.to(dtype=torch.float)
                prediction = self.model.forward(users, movies)
                loss = criterion(prediction, ratings)
                loss.backward()
                optimizer.step()
                if (i % 100) == 0:
                    print(f"batch {i}/{len(data_loader)} loss : {loss}")
