# Thomas McInnes
# CSCI 101 - Section G
# Python Lab 6
# References: None
# Time: 1 hour 30 minutes

import csv

print('Input the name of the file to read math from:')
filename = input('MATHFILE> ')
print('Input the name of the file (in .csv) to output to:')
outputname = input('OUTPUTFILE> ')

with open(filename, 'r') as file:
    math = csv.reader(file, delimiter=',')

    with open(outputname, 'w', newline='') as output:
        writer = csv.writer(output, delimiter=',')

        for i in math:
            counter = 0             # Counter checks what the program should do
            side = 1                # Checks side being evaluated. Side = 1 is left side, side = 2 is right side
            operated = 0
            i.append('==')          # Evaluates the right side of the equation (makes my life easier lol)
            for j in i:
                if len(j) > 1:      # Test for negative numbers
                    if j[1].isdigit() == True:
                        if counter == 0:        # Counter functions explained below
                            num1 = int(j)       # Counter = 0: reads in VERY first number (on the side)
                            counter = 2         # Counter = 1: reading in any numbers past the second (doing math left to right)
                        elif counter == 1:      # Counter = 2: reads in the second number
                            num1 = tempsum      # Counter = 3: Skips reading numbers, does the math and sets a temporary value
                            num2 = int(j)       # Counter = 4: Skips everything and jumps to the final calculation for the side being evaluated
                            counter = 3
                        elif counter == 2:
                            num2 = int(j)
                            counter = 3
                    elif j == '==':
                        counter = 4
                    else:
                        operator = j

                else:       # Test for single digit numbers
                    if j.isdigit() == True:
                        if counter == 0:        # For the very first number on the side
                            num1 = int(j)
                            counter = 2
                        elif counter == 1:      # For later numbers
                            num1 = tempsum
                            num2 = int(j)
                            counter = 3
                        elif counter == 2:
                            num2 = int(j)
                            counter = 3
                    else:
                        operator = j
                
                if counter == 3:                # Does evaluations and sets them to a temporary value (to do the math left to right)
                    if operator == '+':
                        tempsum = num1 + num2
                    if operator == '-':
                        tempsum = num1 - num2
                    if operator == '*':
                        tempsum = num1 * num2
                    if operator == '/':
                        tempsum = num1 / num2
                    if operator == '%':
                        tempsum = num1 % num2
                    if operator == '**':
                        tempsum = num1 ** num2
                    counter = 1
                    operated = 1    # Signifies an operation occured (in case of sides with no evaluations)

                if counter == 4:
                    if side == 1:
                        if operated != 0:      # Checks if the side is just 1 number (if any operations were performed)
                            totalleft = round(tempsum)
                        else:
                            totalleft = round(num1)
                        counter = 0
                        side = 2
                        operated = 0
                    else:
                        if operated != 0:
                            totalright = round(tempsum)
                        else:
                            totalright = round(num1)
                        counter = 0
                        writer.writerow([totalleft,totalright,totalleft==totalright])