#!/usr/bin/python3

if __name__ == '__main__':
    calc_functions = __import__(calculator_1)
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, calc_functions.add(a, b)))
    print('{} - {} = {}'.format(a, b, calc_functions.sub(a, b)))
    print('{} * {} = {}'.format(a, b, calc_functions.mul(a, b)))
    print('{} / {} = {}'.format(a, b, calc_functions.div(a, b)))


