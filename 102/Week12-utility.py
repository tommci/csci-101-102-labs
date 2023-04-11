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

def score_finder(playernames, scores, name):
    j = 0
    for i in playernames:
        if name.lower() == i.lower():
            print(f'OUTPUT {playernames[j]} got a score of {scores[j]}')
            j = 'y'     # For checking if player not found
            break
        j += 1
    if j != 'y':    # if player isn't found, j won't = y
        print('OUTPUT player not found')

def union(list1, list2):
    output_list = []
    for i in list1:
        output_list.append(i)
    for i in list2:
        output_list.append(i)
    return output_list

def intersect(list1, list2):
    output_list = []
    if len(list1) > len(list2):
        for i in list1:
            if i in list2:
                output_list.append(i)
    else:
        for i in list2:
            if i in list1:
                output_list.append(i)
    print(output_list)
    return output_list