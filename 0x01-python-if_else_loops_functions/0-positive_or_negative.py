#!/usr/bin/python3
import random
number = random.randint(-10, 10)
response = ''
if(number > 0):
    response = 'is positive'
elif( number < 0):
    response = 'is negative'
else:
    response = 'is zero'
print(f'{number} {response}')
