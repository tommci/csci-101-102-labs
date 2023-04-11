# Thomas McInnes
# CSCI 102 - Section B
# Assessment 04 Peer Review
# References: None 
# Time: 10 minutes

# Initializes the predetermined lists of elements in each amino acid, as well as the input list
alanine = [3, 7, 1, 2, 0]
arginine = [6, 14, 4, 2, 0]
asparagine = [4, 8, 2, 3, 0]
cysteine = [3, 7, 1, 2, 1]
histidine = [6, 9, 3, 2, 0]
glutamine = [5, 10, 2, 3, 0]
elements_input = []

# Enter values for the elements
print('Enter the elements of the amino acid:\nCARBON> ', end='')
elements_input.append(int(input()))
print('HYDROGEN> ', end='')
elements_input.append(int(input()))
print('NITROGEN> ', end='')
elements_input.append(int(input()))
print('OXYGEN> ', end='')
elements_input.append(int(input()))
print('SULFUR> ', end='')
elements_input.append(int(input()))

# Checks all the existing amino acids against the input. If there's an exact match, it clears, if not, invalid input
if elements_input == alanine:
    print(f'This amino acid is Alanine.\nOUTPUT 3C--7H--1N--2O--0S\nOUTPUT Alanine')
elif elements_input == arginine:
    print(f'This amino acid is Arginine.\nOUTPUT 6C--14H--4N--2O--0S\nOUTPUT Arginine')
elif elements_input == asparagine:
    print(f'This amino acid is Asparagine.\nOUTPUT 4C--8H--2N--3O--0S\nOUTPUT Asparagine')
elif elements_input == cysteine:
    print(f'This amino acid is Cysteine.\nOUTPUT 3C--7H--1N--2O--1S\nOUTPUT Cysteine')
elif elements_input == histidine:
    print(f'This amino acid is Histidine.\nOUTPUT 6C--9H--3N--2O--0S\nOUTPUT Histidine')
elif elements_input == glutamine:
    print(f'This amino acid is Glutamine.\nOUTPUT 5C--10H--2N--3O--0S\nOUTPUT Glutamine')
else:
    print('Invalid input: no match found')