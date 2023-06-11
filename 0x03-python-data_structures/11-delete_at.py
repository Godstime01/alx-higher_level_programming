#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_arr = []
    
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(0, len(my_list)):
        if i != idx:
            new_arr.push(my_list[i])
    return new_arr
