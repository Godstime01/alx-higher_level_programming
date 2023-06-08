#!/usr/bin/python3

def remove_char_at(str, n):
    newStr = ''
    for i in range(len(str)):
        if(i != n):
            newStr += str[i]
    return newStr


if __name__ == "__main__":
    r = remove_char_at('HellWorld', 3)
    print(r)
