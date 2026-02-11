import torch
import torch.nn as nn
import torch.nn.functional as F

class TinyModel(nn.Module):
    def __init__(self, vocab_size, embed_size=16):
        super().__init__()
        self.embed = nn.Embedding(vocab_size+1, embed_size)

        self.fc = nn.Linear(embed_size * 3, vocab_size+1)

    def forward(self, x):

        x = self.embed(x)

        x = x.view(x.size(0), -1)

        logits = self.fc(x)

        return logits
