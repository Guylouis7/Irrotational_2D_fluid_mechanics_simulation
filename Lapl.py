#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""
from getCoeff import getCoeff
import numpy as np
import scipy.sparse as sc
import scipy.sparse.linalg


# Returns an array with the same shape as dom, with 0 where the laplacien is not defined
def laplacien(cl,dom,num):
    data = np.zeros(int(5*np.max(num)))
    rows = np.zeros_like(data)
    cols = np.zeros_like(data)
    Number_of_data = 0
    b_index = 0
    b_vector = np.zeros(int(np.max(num)))

    for x in range(np.shape(dom)[0]): # iterate on all elements of the domain
        for y in range(np.shape(dom)[1]):
            if (dom[x][y]):
                j, a, b = getCoeff(num[x,y-1], num[x,y+1], num[x+1,y], num[x-1,y], num[x,y], dom[x,y], cl[x,y])
               
                len_a = len(a)
                
                data[Number_of_data : Number_of_data + len_a] = np.squeeze(np.asarray(a)) # a is a matrix so we cast it into an array
                rows[Number_of_data : Number_of_data + len_a] = np.full(len_a,(num[x][y] - 1))
                cols[Number_of_data : Number_of_data + len_a] = np.squeeze(np.asarray(j)) - 1 # same
                b_vector[int(num[x][y] - 1)]  = b  
                Number_of_data += len_a
                b_index += 1 
    

    data = data[:Number_of_data] # keep the Number_of_data first elements -> remove last zeros 
    rows = rows[:Number_of_data]
    cols = cols[:Number_of_data]

    A = sc.csc_matrix((data,(rows,cols)),shape = (int(np.max(num)), int(np.max(num)))) 
    sol = scipy.sparse.linalg.spsolve(A,b_vector) 

    # convert sol into a matrix similar to dom
    psi = np.zeros_like(dom)
    for i in range(dom.shape[0]):
        for j in range(dom.shape[1]):
            if dom[i,j] == 0:
                continue
            psi[i,j] = sol[int(num[i,j])-1]
    
    return psi  

                
if __name__ == "__main__":
    dom = np.loadtxt('CL/1-dom.txt')
    num = np.loadtxt('CL/1-num.txt')
    cl = np.loadtxt('CL/1-cl.txt')

    sol = laplacien(cl, dom, num)
    print(sol)     
