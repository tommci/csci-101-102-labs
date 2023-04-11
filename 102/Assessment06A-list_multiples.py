#   Thomas McInnes
#  ​ CSCI 102 – Section B
#   Assessment 06A
#   References: None
#   Time: 5 minutes

j = 1
multiples = []

print('Enter the number to create multiples for:\nNUMBER> ', end='')
num = int(input())
print('Enter the max index of the list of multiples:\nINDEX> ', end='')
index = int(input())

for i in range(0, (index + 1)):     # Calculates the multiple and adds it to the list of multiples
    multiples.append(num * j)
    j += 1

print(f'Your list of multiples is:\nOUTPUT {multiples}\nThe first multiple calculated is:\nOUTPUT {num}')