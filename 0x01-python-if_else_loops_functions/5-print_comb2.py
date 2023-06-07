#!/usr/bin/python3
for num in range(100):
    if(num < 9):
        print(f'{0:d}{num:d}', end=", ")
    elif(num == 99):
        print(num)
    else:
        print(num, end=", ")
