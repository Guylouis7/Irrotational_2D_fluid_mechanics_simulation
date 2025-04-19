#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""

import numpy as np
import matplotlib.pyplot as plt


def section_plot(matrix, title, h,units=""):
    plt.imshow(np.flip(matrix.T, 0) != np.nan, cmap='gray', extent=(0, h*matrix.shape[1], 0, h*matrix.shape[0]), alpha=0.1)
    plt.imshow(np.flip(matrix.T, 0), cmap='plasma', extent=(0, h*matrix.shape[1], 0, h*matrix.shape[0]))
    

    plt.xticks([], [])
    plt.yticks([], [])
    plt.colorbar(label=units)
    plt.title(title)
    plt.show()
    
def vector_field(dom,u,v, psi, U = None, density=0.5):
   
    X, Y = np.meshgrid(np.arange(dom.shape[1]), np.arange(dom.shape[0]))
    plt.imshow(np.flip(np.flip(dom.T, None)) != 0, cmap='gray', extent=(0, dom.shape[1], 0, dom.shape[0]), alpha=0.4)
    plt.contour((np.flip(dom.T, 0)), levels=[2], colors='black', linewidths=4, alpha=0.6)
    strm = plt.streamplot(X,Y,np.flip(v.T, 0), -np.flip(u.T, 0), color=np.flip(U.T, 0), cmap='viridis', density=density,linewidth=0.4, arrowsize=1)
    plt.gca().invert_yaxis()
    plt.colorbar(strm.lines, label='Absolute velocity (m/s)')
    plt.title('Représentation des lignes de courant')
    plt.xticks([], [])
    plt.yticks([], [])
    plt.show()
    
    

    


    
    