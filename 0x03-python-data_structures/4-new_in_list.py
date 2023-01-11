#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1: return my_list

    copy[idx] = element
    return copy
    

if __name__ == "__main__":
    l1 = new_in_list([2,3,4,5,6], 3, 100)
    l2 = new_in_list([2,3,4,5,6], -1, 100)
    print(l1, l2)

