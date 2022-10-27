from random import randint


def matrix(n, m):
    array_2d = []
    for i in range(n):
        internal_array = []
        for j in range(m):
            internal_array.append(randint(1, 20))
        array_2d.append(internal_array)
    return array_2d


def print_matrix(mat):
    for arr in mat:
        for el in arr:
            print(el, end=' ')
        print()
    print('\n')
    for arr in mat:
        arr.reverse()
        for el in arr:
            print(el, end=' ')
        print()


print_matrix(matrix(4, 4))
