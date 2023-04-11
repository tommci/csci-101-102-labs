#   Thomas McInnes
#  ​ CSCI 102 – Section B
#   Week 12 (Git)
#   References:
#   Time:

def load_file(filename):
    with open(filename, 'r') as f:
        content = f.read().splitlines()     # splitlines gets rid of the /n in the output
    return content