# Thomas McInnes
# CSCI 102 - Section B
# Assessment 05
# References: None 
# Time: 10 minutes

print('Enter values to add, and enter quit when finished.')

num = 0
input_list = []

while num != 'quit':
    num = input('NUMBER> ')
    if num != 'quit':
        input_list.append(int(num))

print(f'The addition of the {len(input_list)} numbers entered is:')
print(f'OUTPUT {len(input_list)} numbers\nOUTPUT {sum(input_list)} total')