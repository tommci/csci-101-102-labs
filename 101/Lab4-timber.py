#   Thomas McInnes
#   ​CSCI 101 – Section G
#   Python Lab 4
#   References: none
#   Time: 20 minutes

year_check = 0

print('Enter the number of years of reforestation:\nYEARS> ', end='')
years = int(input())

print('Enter the reforestation rate (percent):\nRATE> ', end='')
rate = (float(input())) / 100

print('Enter the acres remaining after harvest:\nACRES> ', end='')
acres = int(input())

print('| Year | # Acres | % of forest |')

# Calculates and builds the table
for i in range(0, years + 1):
    forest = ((acres / 20000) * 100)
    print(f'OUTPUT {i}, {acres:.1f}, {forest:.2f}%')
    acres = (acres * (1 + rate))
    if year_check != 1:
        if acres > 20000:
            year_check = 1
            final_years = i

# Continues the algorithm to find the total years to restore (without displaying every step)
if year_check != 1:
    while acres < 20000:
        acres = (acres * (1 + rate))
        years += 1
    final_years = years

print(f'It will take {final_years + 1} years to complete reforestation.\nOUTPUT {final_years + 1}')