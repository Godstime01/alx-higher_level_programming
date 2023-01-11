#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0 or idx > len(my_list) - 1: return my_list

    my_list[idx] = element
    return my_list
    

if __name__ == "__main__":
    l1 = new_in_list([2,3,4,5,6], 3, 100)
    print(l1)

