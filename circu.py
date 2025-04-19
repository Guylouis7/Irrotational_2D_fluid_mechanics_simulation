#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""

def circu(u,v,x,y):
    # uses the trapezoidal rule on each segment of the curve
    c = [0] # Circulation
    for i in range(len(u)-1):
        if (x[i+1] != x[i]): # horizontal direction
            c += (u[i] + u[i+1])/2 * (x[i+1] - x[i])

        elif (y[i+1] != y[i]): # vertical direction
            c += (v[i] + v[i+1])/2 * (y[i+1] - y[i])
            
    return c[0]
