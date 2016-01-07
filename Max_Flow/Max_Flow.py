import Functions
import os, math

while (1):
    os.system("cls")
    print("------ Decision of system of the linear equations by the Gauss method ------ \n")
    print("  1) Push relabel maximum flow algorithm;")
    print("  2) Exit from the program; \n")
    index = input("  Enter the necessary point of the menu: ")
    if index == '': index = 0 
    else: index = int(index)
    if index == 1:
        os.system("cls")
        #------------------------------------------------#
        min_G, max_G, n_G = Functions.input_values();
        graf_matrix = Functions.new_rand_graf_matrix(min_G, max_G, n_G);
        #------------------------------------------------#
        os.system("pause")
    elif index == 2:
        os.system("cls")
        break

#os.system("pause")