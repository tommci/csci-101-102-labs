# Thomas McInnes
# CSCI 102 - Section B
# Assessment 07
# References: None
# Time: 20 minutes

insertion_list = []
overall_list = []

print('Enter number of columns:\nCOLUMNS> ', end='')
columns = int(input())
print('Enter number of rows:\nROWS> ', end='')
rows = int(input())
print('Enter the pattern:\nFIRST> ', end='')
pattern1 = input()
print('SECOND> ', end='')
pattern2 = input()

print(f'A checkerboard with {rows} rows, {columns} columns, first string "{pattern1}" and second string "{pattern2}" is:')
for i in range(0, rows):
    if i % 2 == 0:
        for j in range(0, columns):
            if j % 2 == 0:
                insertion_list.append(pattern1)
            else:
                insertion_list.append(pattern2)
    else:
        for j in range(0, columns):
            if j % 2 == 0:
                insertion_list.append(pattern2)
            else:
                insertion_list.append(pattern1)
    print(f'OUTPUT {insertion_list}')
    overall_list.append(insertion_list)
    insertion_list = []
print(f'The 2D array representation is:\nOUTPUT {overall_list}')