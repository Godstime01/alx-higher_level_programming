#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if(i % 15 == 0):
            print('fizzbuzz', end=" ")
        elif(i % 5 == 0):
            print('buzz', end=" ")
        elif(i % 3 == 0):
            print('fizz', end=" ")
        else:
            print(i, end=" ")

if __name__ == '__main__':
    fizzbuzz()
