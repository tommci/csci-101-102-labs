# Thomas McInnes
# CSCI 102 - Section B
# Assessment 01B
# References: Graph paper to determine how to find largest area
# Time: 35 minutes

# Take input of length
print('Enter the length of fencing available in yards:\nLENGTH> ', end='')
length_yards = int(input())

# Converting yards to feet
length_feet = length_yards * 3

# Calculating the max area
area_max = (length_feet / 4)**2

print('The max rectangular area that can be created with the length provided in feet is:')
print('OUTPUT', round(area_max, 1))