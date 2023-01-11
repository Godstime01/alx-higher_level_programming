#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lambda x: x**2, arr)) for arr in matrix]

    return matrix


if __name__ == "__main__":
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    new = square_matrix_simple(matrix)
    print(new)
    print(matrix)
