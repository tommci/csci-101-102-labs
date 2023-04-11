#   Thomas McInnes
#  ​ CSCI 102 – Section B
#   Week 12 (Git)
#   References:
#   Time:

def load_file(filename):
    with open(filename, 'r') as f:
        content = f.read().splitlines()     # splitlines gets rid of the /n in the output
    return content

def update_string(string1, string2, index):
    output_str = ''
    for i in range(0, len(string1)):
        if i == index:
            output_str += string2
        else:
            output_str += string1[i]
    print(f'OUTPUT {output_str}')

def find_word_count(list, word):
    counter = 0
    for i in list:
        wordsplit = []
        wordsplit = i.split(' ')
        for j in wordsplit:
            if j == word:
                counter += 1
    return counter