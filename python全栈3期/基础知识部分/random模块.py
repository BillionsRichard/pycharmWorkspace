import random

print(random.random())
print(random.randint(1,4))
print(random.randrange(1,4))
print(random.choice([1,3,5,'a']))


print(random.sample([1,'a', 2, 'b', 3, 'c'], 2))

print(random.uniform(2,3))

cards = [1,2,3,4]
random.shuffle(cards)
print(cards)