#!/usr/bin/python3
for num in range(100):
    if(num < 10):
        print('0{}'.format(num), end=", ")
    else:
        print('{}{}'.format(num, '' if num == 99 else ','), end=" ")
