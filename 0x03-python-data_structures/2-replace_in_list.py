#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    if idx < 0 or idx > len(my_list) - 1 : return my_list
    my_list[idx] = element
    return my_list

if __name__ == "__main__":
    _ = replace_in_list([3, 5,67,19, 0], 0, 100)
    print(_)
