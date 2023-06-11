#!/usr/bin/python3

def max_integer(my_list=[]):
    max_ = 0
    if  len(my_list) == 0:
        return None
    
    for num in my_list:
        if(num > max_):
            max_ = num
    return max_
