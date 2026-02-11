# model.py

import torch
import torch.nn as nn


class TinyModel(nn.Module):
    """
    A tiny next-token prediction model:
    - Embeds each token
    - Flattens the embeddings
    - Predicts the next token
    """

    def __init__(self, vocab_size, block_size=3, embed_size=16):
        super().__init__()

        # +1 so ID=0 can be padding later if you want
        self.embed = nn.Embedding(vocab_size + 1, embed_size)

        # Input size = block_size * embed_size
        self.fc = nn.Linear(block_size * embed_size, vocab_size + 1)

        self.block_size = block_size

    def forward(self, x):
        # x shape: (batch, block_size)
        x = self.embed(x)               # (batch, block_size, embed_size)
        x = x.view(x.size(0), -1)       # flatten → (batch, block_size*embed_size)
        logits = self.fc(x)             # (batch, vocab_size+1)
        return logits
