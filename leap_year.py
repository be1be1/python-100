"""
input a year, return True if it is lead year, or return false
"""

year = int(input('Please input a year: '))

# We can use \ to split the code if too long
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(is_leap)

# An interesting example: https://techcrunch.com/2008/12/31/zune-bug-explained-in-detail/
# Microsoft the zune bug
