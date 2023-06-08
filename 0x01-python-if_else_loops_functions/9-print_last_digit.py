#!/usr/bin/python3

def print_last_digit(number=-209):
    return number % 10 if number > 0 else (-1 * number )% 10

if __name__ == '__main__':
    r = print_last_digit()
    print(r)
