word_to_id = {}
id_to_word = {}

next_id=1

def tokenize(text):
  global word_to_id, id_to_word, next_id

  word = text.split()
  
  for w in word:
      if w not in word_to_id:
        word_to_id[w] = next_id
        id_to_word[next_id] = w
        
        next_id+= 1
        
  ids = [word_to_id[w] for w in word]
  return ids, word_to_id

def decode(ids):
    words = [id_to_word[i] for i in ids]
    return " ".join(words)
  
ids, vocab = tokenize("hello world hello test world")
print(ids)
print(vocab)

text_back = decode (ids)
print(text_back)

def build_dataset(ids, block_size=3):

    inputs = []
    targets = []

    for i in range(len(ids) - block_size):
        x = ids[i:i+block_size]
        y = ids[i+block_size]
        inputs.append(x)
        targets.append(y)
    return inputs, targets

inputs, targets = build_dataset(ids, block_size=3)
print("Inputs:", inputs)
print("Targets:", targets)
