"""
Calculate the perimeter and area of a circle with input radius
"""
import math

radius = float(input("Please input the radius: "))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2

print('perimeter is: %.2f, area is %.2f' % (perimeter, area))