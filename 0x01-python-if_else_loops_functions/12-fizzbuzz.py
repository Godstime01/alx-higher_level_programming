#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 100):
        if i % 15:
            print("FizzBuzz", end=" ")
        elif i % 5:
            print("Buzz", end=" ")
        elif i % 3:
            print("Fizz", end=" ")
        else:
            print(i, end=" ")
