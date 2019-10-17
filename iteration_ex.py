"""
There are several ways of doing iteration.
"""
# Summation from 0 to 100
sum = 0
for x in range(101):
    sum += x
print(sum)

# Summation from 1 to 100
sum = 0
for x in range(1, 101):
    sum += x
print(sum)

# Summation all even number from 1 to 100
# range(from, to, step size)
sum = 0 
for x in range(2, 101, 2):
    sum += x
print(sum)

# Or we can use
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)



