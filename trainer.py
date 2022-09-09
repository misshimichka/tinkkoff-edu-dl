import torch
from torch.utils.data import DataLoader
from torch import nn
from torch import optim

import numpy as np
from tqdm import tqdm


class TextGenerationTrainer:
    def __init__(self, model, dataset):
        self.model = model
        self.dataset = dataset

    def train(self, args):
        self.model.train()

        dataloader = DataLoader(self.dataset, batch_size=20)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.model.parameters(), lr=0.001)

        for epoch in tqdm(range(60)):
            state_h, state_c = self.model.init_state(5)

            for batch, (x, y) in enumerate(dataloader):
                optimizer.zero_grad()

                y_pred, (state_h, state_c) = self.model(x, (state_h, state_c))
                loss = criterion(y_pred.transpose(1, 2), y)

                state_h = state_h.detach()
                state_c = state_c.detach()

                loss.backward()
                optimizer.step()

            print({'epoch': epoch, 'loss': loss.item()})

        torch.save(self.model, args.input_dir)

    def generate(self, args):
        model = torch.load(args.model)
        model.eval()

        words = args.prefix.split(' ')
        state_h, state_c = model.init_state(len(words))

        for i in range(0, args.length):
            x = torch.tensor([[self.dataset.word_to_index[w] for w in words[i:]]])
            y_pred, (state_h, state_c) = model(x, (state_h, state_c))

            last_word_logits = y_pred[0][-1]
            p = torch.nn.functional.softmax(last_word_logits, dim=0).detach().numpy()
            word_index = np.random.choice(len(last_word_logits), p=p)
            words.append(self.dataset.index_to_word[word_index])

        return words