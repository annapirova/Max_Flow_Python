import Functions as Fun
import os, math, random

graf_matrix, n_G = Fun.file_to_graf_matrix()
Adj, X_Adj, c, GR_list, h, e, f = Fun.graf_matrix_to_graf_list(graf_matrix, n_G)
print("Capacity: ")
Fun.print_graf_list(Adj, X_Adj, c)
print("Flow: ")
Fun.print_graf_list(Adj, X_Adj, f)
Fun.relabel_to_front(e, h, Adj, X_Adj,c, f, n_G) 
os.close(1)