import math, sys, random, queue

def input_values():
    min_tmp = int(input("Enter an interval of values of elements of a matrix \n\nMinimum value: "))
    max_tmp = int(input("\nMaximum value: "))
    n_tmp = int(input("\nQuantity of columns: "))
    print()
    return min_tmp, max_tmp, n_tmp

def new_rand_graf_matrix(min_G_tmp, max_G_tmp, n_G_tmp):

    graf_matrix_tmp = [0] * n_G_tmp
    for i in range(n_G_tmp):
        graf_matrix_tmp[i] = [0] * n_G_tmp

    for i in range(n_G_tmp):
        for j in range(n_G_tmp):
            if (j == 0) or (i == n_G_tmp - 1) or (i == j): graf_matrix_tmp[i][j] = -1
            else: graf_matrix_tmp[i][j] = random.randint(min_G_tmp, max_G_tmp)
        print(graf_matrix_tmp[i])
    print()

    return graf_matrix_tmp

def file_to_graf_matrix():
    f = open('graf_matrix.txt')
    n_G_tmp = 0
    graf_matrix_tmp = []
    for line in f:
        tmp = [int(i) for i in line.split()]
        graf_matrix_tmp.append(tmp)
        n_G_tmp = n_G_tmp + 1
    return graf_matrix_tmp, n_G_tmp
    f.close

def graf_matrix_to_graf_list(graf_matrix_tmp, n_G_tmp):    
    
    Adj_tmp = []
    X_Adj_tmp = []
    c_tmp = []
    GR_list_tmp = queue.Queue()
    h_tmp = [0] * n_G_tmp
    e_tmp = [0] * n_G_tmp
    
    Adj_index_tmp = 0
    XAdj_index_tmp = 0

    for i in range(n_G_tmp):
        for j in range(n_G_tmp):
            if ((graf_matrix_tmp[i][j] != 0) or (graf_matrix_tmp[j][i] != 0)) and (graf_matrix_tmp[j][i] != -1):
                Adj_tmp.append(j)
                c_tmp.append(graf_matrix_tmp[i][j])
                Adj_index_tmp = Adj_index_tmp + 1
        X_Adj_tmp.append(Adj_index_tmp)
        XAdj_index_tmp = XAdj_index_tmp + 1             

    return Adj_tmp, X_Adj_tmp, c_tmp, GR_list_tmp, h_tmp, e_tmp

def print_graf_list(Adj_tmp, X_Adj_tmp, c_tmp, n_G_tmp):
    
    print("1: ") 
    k = 1 
    for i in range(n_G_tmp):
        if i != X_Adj_tmp[k]: print(Adj_tmp[i], "(", c_tmp[i], "), ")   
        else:
            k = k + 1
            print("\n", k + 1, ": ")                    