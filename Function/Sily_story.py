import random

def silly_story():
  """Creates a random and funny story."""
  nouns = ["dog", "banana",  "king"]
  verbs = ["jumped", "sang", "wore"]
  adjectives = ["purple", "squishy", "royal"]

  noun1 = random.choice(nouns)
  verb = random.choice(verbs)
  adjective = random.choice(adjectives)
  noun2 = random.choice(nouns)

  story = f"Once upon a time, there was a {adjective} {noun1}. One day, it {verb} over a {noun2} and laughed!"
  return story

print(silly_story())
