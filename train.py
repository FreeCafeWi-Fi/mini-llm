import torch
import torch.nn as nn
import torch.optim as optim

from tokenizer import tokenize, build_dataset, word_to_id
from model import TinyModel

# 1. Prepare data
ids, vocab = tokenize("hello world hello test world")
inputs, targets = build_dataset(ids, block_size=3)

inputs_tensor = torch.tensor(inputs, dtype=torch.long)
targets_tensor = torch.tensor(targets, dtype=torch.long)

# 2. Build model
vocab_size = len(word_to_id)
model = TinyModel(vocab_size)

# 3. Training setup
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 4. Training loop
for epoch in range(50):
    optimizer.zero_grad()
    logits = model(inputs_tensor)
    loss = loss_fn(logits, targets_tensor)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

with torch.no_grad():
    test_input = torch.tensor([[1, 2, 1]])  # example context
    logits = model(test_input)
    predicted_id = torch.argmax(logits, dim=1).item()
    print("Predicted next word ID:", predicted_id)
    # find word by id
    predicted_word = [w for w, i in word_to_id.items() if i == predicted_id][0]
    print("Predicted word:", predicted_word)
