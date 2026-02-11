def tokenize(text):
  word = text.split()

  word_to_id = {}
  next_id = 1
  for w in word:
      if w not in word_to_id:
        word_to_id[w] = next_id
        next_id+= 1
  ids = [word_to_id[w] for w in word]
  return ids
  
print(tokenize("hello world hello test world"))
