# If we don't know the number of iterations,
# but we know the iteration stopping conditions.
# We can use while loop

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Input: '))
    if number < answer:
        print('Bigger')
    elif number > answer:
        print('Smaller')
    else:
        print('Correct!')
        break
print('You guessed %d times' % counter)
if counter > 7:
    print('Try harder.')