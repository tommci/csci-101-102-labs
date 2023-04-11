# Thomas McInnes, Sean Huber
# CSCI 101 – Section G, B
# Python Lab 7 - Wordle
# References: None
# Time: 70 minutes

'''Opening Messages and Setup'''
# random is a library available to us from the Python Language.
# It lets us generate random or predicted numbers to add
# some variety into our code.
import random

# Prints welcome message
print("Welcome to Wordle!")
print("Here you will provide the length of the words you want to play with and")
print("a random seed value to start the game!")

# The provided dictionary file only has words of certain lengths
valid_lengths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                 15, 16, 17, 18, 19, 20, 21, 22, 24, 28, 29]



# Continues to ask for word_length until the given number is valid
while True:
    print('LENGTH> ',end='')
    word_length = int(input())
    if word_length in valid_lengths:
        break
    else:
        print(f"There are no {word_length}-letter words in the game.")
        print("Please pick again.")

print('SEED> ',end='')
seed = input()

# Uses the entered seed value to 'kickstart' the random number generator
random.seed(seed)


'''Read dictionary, create list of words, choose word to play with'''

# Creates empty list to store words
word_bank = []

# Open the file based on the given name ("dictionary.txt"), in read mode ('r'),
# and interpret the binary data using the utf-8 protocol.
# Assign the file to a variable called 'dictionary_file'.

with open('dictionary.txt', 'r') as dictionary_file:
    # read the entire file as a single string and store into a variable
    file = dictionary_file.read()

'''After and outside of the with statement on line 60 above,
the document is closed automatically'''


dictionary = file.split()



# For each word in the list
for word in dictionary:
    # If the word is the desired length
    if len(word) == word_length:
        # Add it to our word bank for the game
        word_bank.append(word)


# Uses the random generator to pick one word from the list to play with.
# random.choice(list) takes in a list and returns one randomly chosen value.

secret_word = random.choice(word_bank)


# Uncomment the next line to see what words were found, if you'd like.
# print(f"Word bank:\n{word_bank}")

# Uncomment the next line to see what word was randomly picked, if you'd like.
# print(f"Secret word: {secret_word}")


'''Setup Play'''
# Players are allowed 6 tries to guess the secret word
num_guesses_allowed = 6

# Players start with 0 guesses made
num_guesses_used = 0

# Until the word is guessed, or the number of tries has run out, keep playing.
# The game is not over yet, so game_result is a placeholder None for now
game_result = None

# Creates an empty list to store the guesses
guess_list = []

'''Start Play'''
# While we can still play
while game_result is None:
    
    '''Collect Valid Guess'''    
    # Continues to ask the player for new_guess until:
    # the guess is the right size,
    # the guess is a real word,
    # and the guess hasn't been used before.
    # When all the conditions are true, new_guess is valid.
    guess_is_valid = False
    while guess_is_valid == False:

        # Collects a new guess from the player
        print('GUESS> ',end='')
        new_guess = input()

        # Forces all letters to lowercase, just in case
        new_guess = new_guess.lower()

        # Check if new_guess length isn't valid
        if len(new_guess) != word_length:
            print(f"Please enter a {word_length}-letter word.")

        # Check if new_guess isn't a real word (exists in word_bank)
        elif new_guess not in word_bank:
            print(f"Please enter a real word.")

        # Check if new_guess has been used before (exists in guess_list)
        elif new_guess in guess_list:
            print(f"Please enter a word you haven't guessed yet.")

        else:
            guess_is_valid = True

    # Creates list for the result of this guess and fills with placeholders '_'
    result_list = list('_' * word_length)

    # Creates a list of the secret word characters to work with.
    # (We use a list here instead of a string, because it's easier
    # to change individual characters of a list.)
    secret_list = list(secret_word)

    '''Generate Guess Results'''
    
    

    '''Check for all exact matches (right letter right spot)'''    
    # For each index i in the new_guess
    for i in range(0, len(new_guess)):

        # Uncomment the next line to help with debugging
        # print(f"Searching for a match at index {i}...")
        # If new_guess at i is equal to secret_list at i
        if new_guess[i] == secret_list[i]:

            # It's an exact match!
            # Uncomment the next line to help with debugging
            # print("Match found!")
            # result_list at index i should be changed to 'x'
            result_list[i] = 'x'

            # secret_list at index i should be changed to '_' to avoid double matches
            secret_list[i] = '_'
            
            # Uncomment the next line to help with debugging
            # print(f"Current results: {result_list}")

    '''Check for inexact matches (right letter wrong spot)'''    
    # For each index i in the new_guess
    for i in range(0, len(new_guess)):

        # If we've already matched this letter, result_list here will be 'x'
        # and you should skip to the next index i
        if result_list[i] == 'x':
            continue


        else:

            # Uncomment the next line to help with debugging
            # print(f"Searching for a match for character {new_guess[i]}")

            # For each index j in the secret_list
            for j in range(0, len(secret_list)):

                # If new_guess at i is equal to secret_list at j
                if new_guess[i] == secret_list[j]:

                    # Letter exists in secret word!
                    # Uncomment the next line to help with debugging
                    # print("Match found!")
                    # result_list at i should be changed to 'o'
                    result_list[i] = 'o'

                    # secret_list at j should be changed to '_', like before
                    secret_list[j] = '_'
                
                    # Uncomment the next line to help with debugging
                    # print(f"Current results: {result_list}")

                    # skip the rest of the j loops
                    break

    
    # It would be easier for the player to see result_list as a string.
    # This creates a string from all entries in a given list,
    # with spaces separating each entry for clarity.
    print(f"OUTPUT {' '.join(result_list)}")

    guess_list.append(new_guess)
    # This helps to make sure the player doesn't guess the same thing twice
    
    
    num_guesses_used += 1
    
    
    '''Win/Loss Conditions'''
    # If all characters are exact matches in the right spot
    # The latest guess will be exactly equal to the secret word
    # and the game is over

    if new_guess == secret_word:
        game_result = 'Won'



    # The game might also be over if the player is out of guesses

    elif num_guesses_used == num_guesses_allowed:
        game_result = 'Lost'


'''Final Results'''
# If we reach this line of code, the game is over; we've exited the while loop.
print("Game over.")

# Print statements without OUTPUT aren't graded, but they are helpful.
# Checks the game_result and tells the player
# TODO: Add If statements to print final game results
if game_result == 'Won':
    print(f"Congratulations!")
    print(f"You guessed the word '{secret_word}' in {num_guesses_used} guesses!")
    print("You win!")
elif game_result == 'Lost':
    print(f"You were not able to guess the word '{secret_word}'.")
    print("You lose.")


print(f"OUTPUT {secret_word}")
print(f"OUTPUT {game_result}")