# Thomas McInnes
# CSCI 102 - Section B
# Assessment 02
# References: None
# Time: 15 minutes

# Inputting the initial string
print('Input a string:\nSTRING> ', end='')
string =  input()
a_slice = ()
b_slice = ()
c_slice = ()
d_slice = ()

# Inputting slices
print('Enter four numbers to slice inputted string:\nA> ', end='')
a_slice = int(input())
print('B> ', end='')
b_slice = int(input())
print('C> ', end='')
c_slice = int(input())
print('D> ', end='')
d_slice = int(input())

# Output as directed (not including entered values, just between them)
print(f'OUTPUT {string[(a_slice + 1):b_slice]} {string[(c_slice + 1):d_slice]}')