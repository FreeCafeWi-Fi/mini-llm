def tokenize(text):
next_id = 1

def tokenize(text):
  global word_to_id, next_id

  words = text.split()
  
  for w in word:
      if w not in word_to_id:
        word_to_id[w] = next_id
        next_id+= 1
        
  ids = [word_to_id[w] for w in word]
  return ids, word_to_id
  
ids, vocab = tokenize("hello world hello test world")
print(ids)
print(vocab)

