#!/usr/bin/python3

add = __import__("add").add

if __name__ == '__main__':
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")
