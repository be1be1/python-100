value = float(input('Please input the length: '))
unit = str(input('Please input the unit: '))

# Please notice that you should use two comparison operator == to 
# to check the unit. If you write unit == 'in' or '英寸', 
# unit == ('in' or '英寸'), it always return true. 
# See http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/boolean.html 
# for the boolean value of other datatypes.
if unit == 'in' or unit == '英寸':
    print('%.2f inch = %.2f cm' % (value, value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f cm = %.2f in' % (value, value/2.54))
else:
    print('Input a correct unit!!!')
