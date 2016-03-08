import Functions as Fun
import os, math

while (1):
    os.system("cls")
    print("------ Algorithms on graphs: search of the maximum flow ------ \n")
    print("  1) Push relabel algorithm;")
    print("  2) Exit from the program; \n")
    index = input("  Enter the necessary point of the menu: ")
    if index == '': index = 0 
    else: index = int(index)
    if index == 1:
        os.system("cls")
        #------------------------------------------------#
        graf_matrix, n_G = Fun.file_to_graf_matrix()
        Adj, X_Adj, c, GR_list, h, e, f = Fun.graf_matrix_to_graf_list(graf_matrix, n_G)
        print("Capacity: ")
        Fun.print_graf_list(Adj, X_Adj, c)
        print("Flow: ")
        Fun.print_graf_list(Adj, X_Adj, f)
        Fun.init_bfs(n_G - 1, e, h, Adj, X_Adj, c, f)
        print("e =",e)
        print("h =",h)
        print()
        print("Answer: ")
        i = 1
        Fun.discharge(i, e, h, Adj, X_Adj, c, f)
        Fun.print_graf_list(Adj, X_Adj, f)        
        print("e =",e)
        print("h =",h)
        print()
        #------------------------------------------------#
        os.system("pause")
    elif index == 2:
        os.system("cls")
        break

#os.system("pause")