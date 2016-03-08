import math, sys, random, queue

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
            if graf_matrix_tmp[i][j] != -1:
                Adj_tmp.append(j)
                c_tmp.append(graf_matrix_tmp[i][j])
                Adj_index_tmp = Adj_index_tmp + 1
        X_Adj_tmp.append(Adj_index_tmp)
        XAdj_index_tmp = XAdj_index_tmp + 1             

    f_tmp = [0] * len(Adj_tmp)

    return Adj_tmp, X_Adj_tmp, c_tmp, GR_list_tmp, h_tmp, e_tmp, f_tmp

def print_graf_list(Adj_tmp, X_Adj_tmp, c_tmp):
    
    print("0: ", sep = '', end = '') 
    k = 0; i = 0
    while i != len(Adj_tmp):
        if i != X_Adj_tmp[k]: print(Adj_tmp[i], "(", c_tmp[i], "), ", sep = '', end = '')   
        else:
            k = k + 1            
            print("\n", k, ": ", sep = '', end = '')   
            print(Adj_tmp[i], "(", c_tmp[i], "), ", sep = '', end = '') 
        i = i + 1
    print(); print()

def add_f(value, u, v, Adj_tmp, X_Adj_tmp, f_tmp):
    
    if u != 0: i = X_Adj_tmp[u - 1] 
    else: i = 0
    
    while 1 == 1:
        if Adj_tmp[i] == v: break
        i = i + 1
     
    f_tmp[i] = value   

def get_f(u, v, Adj_tmp, X_Adj_tmp, f_tmp):
    
    if u != 0: i = X_Adj_tmp[u - 1] 
    else: i = 0
    
    while 1 == 1:
        if Adj_tmp[i] == v: break
        i = i + 1  
    
    return f_tmp[i]  

def c_f(u, v, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp):
    
    c = get_f(u, v, Adj_tmp, X_Adj_tmp, c_tmp)    
    f = get_f(u, v, Adj_tmp, X_Adj_tmp, f_tmp)
    return c - f

def push(u, v, e, h, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp):
    
    d = min(e[u], c_f(u, v, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp))
    flow = get_f(u, v, Adj_tmp, X_Adj_tmp, f_tmp)
    add_f(flow + d, u, v, Adj_tmp, X_Adj_tmp, f_tmp)
    neg_flow = get_f(u, v, Adj_tmp, X_Adj_tmp, f_tmp)
    flow = get_f(v, u, Adj_tmp, X_Adj_tmp, f_tmp)
    add_f(flow - neg_flow, v, u, Adj_tmp, X_Adj_tmp, f_tmp)
    e[u] = e[u] - d; e[v] = e[v] + d

def relabel(u, e, h, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp):
    
    adj_list = adjacency(u, Adj_tmp, X_Adj_tmp)
    tmp = []
    i = 0
    while i < len(adj_list):
        v = adj_list[i]
        if h[u] <= h[v]: tmp.append(h[v])
        i = i + 1
    h[u] = min(tmp) + 1        

def adjacency(u, Adj_tmp, X_Adj_tmp):
    
    adj_list = []

    if u == 0: i = 0; j = X_Adj_tmp[0]
    else: i = X_Adj_tmp[u - 1]; j = X_Adj_tmp[u]        

    while i < j:
        adj_list.append(Adj_tmp[i])
        i = i + 1
    
    return adj_list     

def init_bfs(u, e, h_tmp, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp):

    Q = queue.Queue()
    Q.put(u)
    old = []
    while not Q.empty():
        v = Q.get()
        old.append(v)
        adj_list = adjacency(v, Adj_tmp, X_Adj_tmp)
        i = 0
        while i < len(adj_list):
            y = adj_list[i]
            if old.count(y) == 0: 
                Q.put(y)
                h_tmp[y] = h_tmp[v] + 1
            i = i + 1
    list_per_flow = adjacency(0, Adj_tmp, X_Adj_tmp)  
    i = 0
    while i < len(list_per_flow):
        u = list_per_flow[i]
        value = get_f(0, u, Adj_tmp, X_Adj_tmp, c_tmp)
        add_f(value, 0, u, Adj_tmp, X_Adj_tmp, f_tmp)
        add_f(-value, u, 0, Adj_tmp, X_Adj_tmp, f_tmp)
        e[u] = value
        e[0] = e[0] - value
        i = i + 1

def discharge(u, e, h, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp):
    
    adj_list = adjacency(u, Adj_tmp, X_Adj_tmp)
    i = 0
    while i < len(adj_list):
        v = adj_list[i]
        if i == len(adj_list)-1: 
            relabel(u, e, h, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp)
            i = i + 1
        elif ((c_f(u, v, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp) > 0) and (h[u] == h[v] + 1)):  push(u, v, e, h, Adj_tmp, X_Adj_tmp, c_tmp, f_tmp)
        else: i = i + 1