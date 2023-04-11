# Thomas McInnes
# CSCI 101 - Section G
# Python Lab 3
# References: None
# Time: 30 minutes

# Initialize variables, set up valid characters
valid_chars = ['X', 'O', 'E']
row1 = input('ROW1> ')
row2 = input('ROW2> ')
row3 = input('ROW3> ')

# Check for errors (if string is too long/short, or if invalid character exists)
if (len(row1) != 3) or (len(row2) != 3) or (len(row3) != 3):
    print('OUTPUT ERROR')
elif (row1[0] not in valid_chars) or (row1[1] not in valid_chars) or (row1[2] not in valid_chars):
    print('OUTPUT ERROR')
elif (row2[0] not in valid_chars) or (row2[1] not in valid_chars) or (row2[2] not in valid_chars):
    print('OUTPUT ERROR')
elif (row3[0] not in valid_chars) or (row3[1] not in valid_chars) or (row3[2] not in valid_chars):
    print('OUTPUT ERROR')

# If there are no errors, check to see who wins
else:
    if ((row1[0] == row1[1] == row1[2]) and (row1[0] != 'E')):      # Checks for row winners
        print(f'OUTPUT {row1[1]}')
    elif ((row2[0] == row2[1] == row2[2]) and (row2[0] != 'E')):
        print(f'OUTPUT {row2[1]}')
    elif ((row3[0] == row3[1] == row3[2]) and (row3[0] != 'E')):
        print(f'OUTPUT {row3[1]}')

    elif ((row1[0] == row2[0] == row3[0]) and (row2[0] != 'E')):    # Checks for column winners
        print(f'OUTPUT {row2[0]}')
    elif ((row1[1] == row2[1] == row3[1]) and (row2[1] != 'E')):
        print(f'OUTPUT {row2[1]}')
    elif ((row1[2] == row2[2] == row3[2]) and (row2[2] != 'E')):
        print(f'OUTPUT {row2[2]}')

    elif (row1[0] == row2[1] == row3[2]) or (row1[2] == row2[1] == row3[0]):    # Checks for diagonal winners
        if row2[1] == 'E':
            print('OUTPUT T')
        else:
            print(f'OUTPUT {row2[1]}')
    else:
        print('OUTPUT T')                # If there are no winners AND the code doesn't error before this point, then it must be a tie

