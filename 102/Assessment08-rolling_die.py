#   Thomas McInnes
#  ​ CSCI 102 – Section B
#   Assessment 08
#   References: None
#   Time: 10 minutes

import random

print('Input the RNG seed:\nSEED> ', end='')
seed = int(input())
print('Input the amount of rolls to make:\nROLLS> ', end='')
rolls = int(input())
print('Input the amount of sides on the die:\nSIDES> ', end='')
sides = int(input())

random.seed(seed)
results = []

for i in range(0, rolls):
    results.append(random.randint(1, sides))

for i in range(1, sides+1):
    print(f'OUTPUT {i} occurred {results.count(i)} times')