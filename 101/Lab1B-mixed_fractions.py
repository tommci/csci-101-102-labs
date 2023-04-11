# Thomas McInnes
# CSCI 101 - Section G
# Python Lab 1B
# References: Zybooks section 15.7
# Time: 15 minutes

# Taking inputs
print('Input the numerator of the improper fraction.\nNUMERATOR> ', end='')
numerator = int(input())
print('Input the denominator of the improper fraction.\nDENOMINATOR> ', end='')
denom = int(input())

# Calculations
whole_num = numerator // denom # This finds the whole number of the mixed fraction
mixed_numer = numerator % denom # This finds the new numerator for the mixed fraction

# Output
print(f'{numerator}/{denom} as a mixed fraction is:')
print(f'OUTPUT {whole_num} {mixed_numer}/{denom}')