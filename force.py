#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""


def force(p,x,y):
    # uses the trapezoidal rule on each segment of the curve
    fx = 0
    fy = 0
    for i in range(len(p)-1):
        if (x[i+1] != x[i]): # horizontal direction
            fy += (p[i] + p[i+1])/2 * (x[i] - x[i+1])

        elif (y[i+1] != y[i]): # vertical direction
            fx += (p[i] + p[i+1])/2 * (y[i+1] - y[i])
            
    return fx[0],fy[0]