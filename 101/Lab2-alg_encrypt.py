# Thomas McInnes
# CSCI 101 - Section G
# Python Lab 2
# References: CSCI 102 Studio 2 Problem 5
# Time: 30 minutes

# Takes inputs and converts them to strings for manipulation
print('Input five lists of characters:\nLIST1> ', end='')
inpt1 = str(input())
print('LIST2> ', end='')
inpt2 = str(input())
print('LIST3> ', end='')
inpt3 = str(input())
print('LIST4> ', end='')
inpt4 = str(input())
print('LIST5> ', end='')
inpt5 = str(input())

# Encrypts each given input as specified (except input 5)
encrypt1 = inpt1[-2:] + inpt1[0:(len(inpt1) - 2)]
encrypt2 = inpt2[0:-2]
encrypt3 = inpt3[(len(inpt3) // 2):]
encrypt4 = inpt4[0:2] + inpt4[4] + inpt4[3:4] + inpt4[2] + inpt4[5:]

# Prints the output and handles input 5
print(f'OUTPUT {inpt5[0:2]} {encrypt1}{encrypt2}{encrypt3}{encrypt4} {inpt5[2:]}')