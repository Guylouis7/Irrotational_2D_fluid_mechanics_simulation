#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import *
from scipy.optimize import bisect

def J_bottom_v_horiz(kutta_percentage):
    h = 0.01
    dom = np.loadtxt('CL/2-dom.txt')
    kutta_dom = np.loadtxt('CL/kutta.txt')
    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
    coord_obstacle= np.loadtxt('CL/2-contourObj.txt').astype(int)
    num = np.loadtxt('CL/2-num.txt')

    cl = compute_cl(dom, dom_bords, coord_obstacle, 0.5, 0.01, kutta_percentage)
    velocity_matrices = velocity(h,cl,dom,num)
    
    i, j = np.where(kutta_dom == 3)
    i, j = i[0], j[0]
    print("Percentage : ", kutta_percentage, ", horizontal speed : ", velocity_matrices[2][i][j])
    return velocity_matrices[2][i][j]  #matrix u, horizontal speed at the bottom of the obstacle
    
    
def J_CL_Kutta():
    a = 0.5
    b = 0
    cl_percentage = bisect(J_bottom_v_horiz, a, b)
    print("Final percentage : ", cl_percentage)
    
    return cl_percentage
    
    
if __name__ == "__main__":
    configuration_obstacle(0.5, J_CL_Kutta())