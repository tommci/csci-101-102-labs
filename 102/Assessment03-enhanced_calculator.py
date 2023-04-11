# Thomas McInnes
# CSCI 102 - Section B
# Assessment 03
# References: None 
# Time: 30 minutes

# Initializing variables
operand_one = 0.0
operand_two = 0.0
operation = 0
sum = 0.0
difference = 0.0
product = 0.0
quotient = 0.0
remainder = 0.0

# Taking inputs
print('Input an operand.\nFIRST> ', end='')
operand_one = float(input())
print('Input a second operand.\nSECOND> ', end='')
operand_two = float(input())
print('Choose an operation by typing its corresponding number:\n1: addition\n2: subtraction\n3: multiplication\n4: division')
print('OPERATION> ', end='')
operation = int(input())

# Calculates the operation based on the selection
if operation == 1:
    sum = operand_one + operand_two
    print(f'Answer: {sum:.6f}\nOUTPUT {sum:.6f}')
elif operation == 2:
    difference = operand_one - operand_two
    print(f'Answer: {difference:.6f}\nOUTPUT {difference:.6f}')
elif operation == 3:
    product = operand_one * operand_two
    print(f'Answer: {product:.6f}\nOUTPUT {product:.6f}')
elif operation == 4:
    quotient = int(operand_one // operand_two)
    remainder = int(operand_one % operand_two)
    print(f'Answer: {quotient} quotient and {remainder} remainder')
    print(f'OUTPUT {quotient}\nOUTPUT {remainder}')

#If a selection is made outside the options (1 - 4) this message prints
else:
    print('Invalid input for operation. Please try again.')