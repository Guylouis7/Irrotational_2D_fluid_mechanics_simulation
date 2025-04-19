#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""

import numpy as np

def getCoeff(num_left,num_right,num_down,num_up,num_cent,type_cent,cl_cent):
    
    if (type_cent == 0): # outside of the domain
        a = np.zeros(5)
        j = np.zeros_like(a)
        b = 0
        
    if (type_cent == 1): # node surrounded by calculation nodes or boundary conditions
        a = np.array([1, 1, 1, 1, -4])
        b = 0
        j = np.array([num_left,num_right,num_down,num_up,num_cent])
        
        
    if (type_cent == 2): # Dirichlet boundary condition node
        a = np.array([1])
        b = cl_cent
        j = np.array([num_cent])
        
        
    a = np.reshape(a,(-1,1))
    j = np.reshape(j,(-1,1))
    
    return j,a,b

