# tokenizer.py

import json

word_to_id = {}
id_to_word = {}
next_id = 1  # 0 can be reserved for padding if you want later


def tokenize(text):
    """
    Build/update vocab from text and return list of ids.
    """
    global word_to_id, id_to_word, next_id

    words = text.split()

    for w in words:
        if w not in word_to_id:
            word_to_id[w] = next_id
            id_to_word[next_id] = w
            next_id += 1

    ids = [word_to_id[w] for w in words]
    return ids, word_to_id


def decode(ids):
    """
    Convert list of ids back to a space-separated string.
    """
    words = [id_to_word[i] for i in ids]
    return " ".join(words)


def build_dataset(ids, block_size=3):
    """
    Turn a sequence of ids into (inputs, targets) pairs
    for next-token prediction with context length = block_size.
    """
    inputs = []
    targets = []

    for i in range(len(ids) - block_size):
        x = ids[i:i + block_size]
        y = ids[i + block_size]
        inputs.append(x)
        targets.append(y)

    return inputs, targets


def save_vocab(path):
    """
    Save vocab to disk as JSON.
    """
    data = {
        "word_to_id": word_to_id,
        "id_to_word": id_to_word,
        "next_id": next_id,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_vocab(path):
    """
    Load vocab from disk.
    """
    global word_to_id, id_to_word, next_id

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    word_to_id = {k: int(v) for k, v in data["word_to_id"].items()}
    id_to_word = {int(k): v for k, v in data["id_to_word"].items()}
    next_id = int(data["next_id"])
