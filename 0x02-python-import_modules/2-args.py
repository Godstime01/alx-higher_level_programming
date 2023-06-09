#!/usr/bin/python3
import sys

length_of_arg = len(sys.argv)
if(length_of_arg < 2):
    print('{}'.format(0))
else:
    print('{} {}:'.format(length_of_arg - 1, 'argument' if length_of_arg < 3 else 'arguments'))

    for i in range(1, length_of_arg):
        print('{}: {}'.format(i, sys.argv[i]))
