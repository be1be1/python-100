# This method is called Heron's formula
# Check: https://en.wikipedia.org/wiki/Heron%27s_formula

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('perimeter: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('area: %f' % (area))
else:
    print('No triangle formed')