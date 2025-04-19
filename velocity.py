#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""

import numpy as np
from Lapl import laplacien
from deriv import deriv
from section_plot import section_plot

def velocity(h,cl,dom,num):
    psi = laplacien(cl, dom, num)
    #section_plot(psi, "psi", h)
    dim_dom = np.shape(dom)
    
    u = np.empty_like(dom)
    v = np.empty_like(dom)
    
    for coord_y in range(dim_dom[1]): # coord_y = i
        for coord_x in range(dim_dom[0]): # coord_x = j

            if int(num[coord_y,coord_x]) == 0 :
                u[coord_y,coord_x] = np.nan
                v[coord_y,coord_x] = np.nan
               
            else : 
                type_c      = dom[coord_y, coord_x]
                type_left   = dom[coord_y, coord_x-1]
                type_right  = dom[coord_y, coord_x+1]
                type_down   = dom[coord_y-1, coord_x]
                type_up     = dom[coord_y+1, coord_x]
 
                
                
                f_c     = psi[coord_y, coord_x]
                
                f_left = 0
                f_right = 0
                f_up = 0
                f_down = 0
                
                if type_left:
                    f_left  = psi[coord_y, coord_x-1]
                    
                if type_right:
                    f_right = psi[coord_y, coord_x+1]
                
                if type_down:
                    f_down  = psi[coord_y-1, coord_x]
                    
                if type_up:
                    f_up    = psi[coord_y+1, coord_x]
                
                v[coord_y,coord_x] = - deriv(f_left, f_c, f_right, type_left, type_c, type_right, h)
                u[coord_y,coord_x] = deriv(f_down, f_c, f_up, type_down, type_c, type_up, h)
                
    U = np.sqrt(u**2 + v**2)
    return U,u,v, psi
    
if __name__ == '__main__':
    from section_plot import vector_field
    h = 0.5
    dom = np.loadtxt('CL/1-dom.txt')
    print("Domain :")
    print(dom)
    print()

    num = np.loadtxt('CL/1-num.txt')
    print("Num :")
    print(num)
    print()

    cl = np.loadtxt('CL/1-cl.txt')

    print("CL :")
    print(cl)
    print(velocity(h,cl,dom,num))
    section_plot(velocity(h,cl,dom,num)[0], "Absolute velocity", h)

    vector_field(dom,velocity(h,cl,dom,num)[1],velocity(h,cl,dom,num)[2])