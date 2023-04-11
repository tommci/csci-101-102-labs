#   Thomas McInnes
#  ​ CSCI 102 – Section B
#   Assessment 11
#   References: Google to find equation for cylinder and conversions to polar coordinates
#   Time: 20 minutes 

import math

def print_output(output):
    print(f'OUTPUT {output}')

def cylinder_vol(radius, height):
    print_output(f'{((3.1415) * (radius ** 2) * (height)):.2f}')

def lbs_to_kg(lbs):
    print_output(f'{(lbs * 0.4536):.4f}')

def polar_coords(x,y):
    print_output(f'r: {(math.sqrt((x ** 2) + (y ** 2))):.2f}')      # r = the square root of x^2 + y^2
    print_output(f'theta: {math.degrees((math.atan(y / x))):.2f}')  # theta = arctan(y/x) (in radians, convert to degrees with math.degrees)

def yen_to_dollars(yen):
    print_output(f'{(yen * 0.0068):.2f}')

def quad_form(a,b,c):
    x1 = int(((b * -1) + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a))    # x = (-b +- sqrt(b^2-4ac))/2a
    x2 = int(((b * -1) - (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a))
    if x1 < x2:
        print_output(f'{x1}')
        print_output(f'{x2}')
    else:
        print_output(f'{x2}')
        print_output(f'{x1}')