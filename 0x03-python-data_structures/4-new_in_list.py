#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy_arr = my_list

    if idx < 0 or idx > len(my_list):
        return copy_arr
    copy_arr[idx] = element
    return copy_arr
