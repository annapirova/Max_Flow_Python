import math, sys, random

def input_values():
    min_tmp = int(input("Enter an interval of values of elements of a matrix \n\nMinimum value: "))
    max_tmp = int(input("\nMaximum value: "))
    n_tmp = int(input("\nQuantity of columns: "))
    print()
    return min_tmp, max_tmp, n_tmp

def new_rand_graf_matrix(min, max, n):

    graf_matrix_tmp = [0] * n
    for i in range(n):
        graf_matrix_tmp[i] = [0] * n

    for i in range(n):
        for j in range(n):
            if (j == 0) or (i == n-1) or (i == j): graf_matrix_tmp[i][j] = 0
            else: graf_matrix_tmp[i][j] = random.randint(min, max)
        print(graf_matrix_tmp[i])
    print()

    return graf_matrix_tmp