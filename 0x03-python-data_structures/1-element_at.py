#!/usr/bin/python3


def element_at(my_list, idx):

    if idx < 0 or idx > len(my_list): return None
    return my_list[idx]

if __name__ == "__main__":
    elem = element_at([1,2,3,4,6, 10], 5)
    elem1 = element_at([1,2,3,4,6, 10], -1)
    elem2 = element_at([1,2,3,4,6, 10], 10)
    print(elem, elem1, elem2)

