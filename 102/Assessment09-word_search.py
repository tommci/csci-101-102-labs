#   Thomas McInnes
#  ​ CSCI 102 – Section B 
#   Assessment 09
#   References: Prof Mark Baldwin helped with the bounds of the randint.() argument
#   Time: 50 minutes

import random

file = open('dictionary.txt')
words = file.readlines()
file.close()

print('Enter your random number seed:\nSEED> ', end='')
seed = input()
print('Enter the number of letters in the word to search for:\nLENGTH> ', end='')
length = int(input())

random.seed(seed)
matching = []

for i in words:
    if (len(i) - 1) == length:      # Using len(i) appends all words with a length of 5. Subtracting 1 from len(i) fixes this
        matching.append(i)
    
if len(matching) > 1:
    print(f'A random word with {length} letters is:\nOUTPUT {matching[random.randint(0, len(matching)-1)]}', end='')
    print(f'There are {len(matching)} words {length} letters long.\nOUTPUT {len(matching)}')
elif len(matching) == 1:
    print(f"Cool! There's only one word with {length} letters! It's this:\nOUTPUT {matching[random.randint(0, len(matching)-1)]}", end='')
    print(f'OUTPUT 1')
else:
    print(f"There aren't any words with {length} letters in the dictionary we're using.\nOUTPUT None\nOUTPUT 0")