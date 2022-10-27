from random import randint


def matrix(n, m):
    array_2d = []
    for i in range(n):
        internal_array = []
        for j in range(m):
            internal_array.append(randint(1, 10))
        array_2d.append(internal_array)
    return array_2d


def sum_matrix(mat1):
    for arr in mat1:
        for el in arr:
            print(el, end=' ')
        print()
    for i in range(len(mat1)):
        i1 = i - 1
        stroki2 = 0
        for j in range(len(mat1[2])):
            stroki2 += mat1[i1][j]
    for k in range(len(mat1)):
        k1 = k
        stroki3 = 0
        for m in range(len(mat1[3])):
            stroki3 += mat1[k1][m]

    return f'сумма 2й строки {stroki2}сумма 3й строки{stroki3}'


x = matrix(4, 4)
print(x)
print(sum_matrix(x))
