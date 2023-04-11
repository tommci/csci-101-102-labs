#   Thomas McInnes
#   CSCI 101 – Section G
#   Python Assessment 3
#   References: Zybooks file I/O and string formatting sections
#   Time: 20 minutes

import string

# Sets up variables and lists needed later. Since numbers are ignored, they're removed here for the sake of readable code later
punc = string.punctuation + string.digits
fulltext_split = []
unique_words = []
count = 0

# Opens the file, enters it into the fulltext object, then closes it
file = open('Pride&Prejudice_Ch1&2.txt')
fulltext = file.read()
file.close()

# Replaces hyphens with spaces, removes punctuation, and makes everything lowercase, in that order
fulltext = fulltext.replace('-', ' ')
for i in punc:
    if i in fulltext:
        fulltext = fulltext.replace(i, '')
fulltext = fulltext.lower()

# Splits the document into a list, with each entry as each word in the document
fulltext_split = fulltext.split(' ')

# Select a choice UI
print('Select an option:\n1: Find the number of times a specifc word appears\n2: Find the number of words of a specific length\nOPTION> ', end='')
choice = int(input())

# Handles option 1. Turns the user's input lowercase, then searches the list word by word. If the words match, count increased.
if choice == 1:
    print('Enter a word to search for:\nWORD> ', end='')
    word = input().lower()
    for i in fulltext_split:
        if i == word:
            count += 1
    print(f'The word "{word}" appears {count} times in the document.\nOUTPUT {count}')

# Handles option 2. Compares each word length to the length input. If they match, count increased. If the word isn't in the unique words list, it's added.
elif choice == 2:
    print('Enter the length of words to search for:\nLENGTH> ', end='')
    length = int(input())
    for i in fulltext_split:
        if len(i) == length:
            count += 1
            if i not in unique_words:
                unique_words.append(i)
    print(f'There are {count} words with length {length} in the document.\nOUTPUT {count}')
    print(f'There are {len(unique_words)} unique words with length {length} in the document.\nOUTPUT {len(unique_words)}')

# If 1 or 2 isn't input, error
else:
    print('Invalid selection. Please enter 1 or 2.\nOUTPUT ERROR')