def tokenize(text):
  word = text.split()

  word_to_id = {"hello": 1, "world": 2}

  ids = [word_to_id[w] for w in word]

  return ids
  
print(tokenize("hello world hello"))
