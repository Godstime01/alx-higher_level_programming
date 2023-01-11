#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    my_list.reverse()
    for content in my_list:
        print("{:d}".format(content))

if __name__ == "__main__":
    print_reversed_list_integer([1,2,3,4,5,6])
