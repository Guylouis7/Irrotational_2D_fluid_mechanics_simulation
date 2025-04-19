#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""
import numpy as np

def deriv(f_left, f_c, f_right, type_left, type_c, type_right, h):
    if (not(type_c) or (not(type_left) and not(type_right))): # error if not in domain
        return np.nan 
     
    if (not(type_left) and type_right):  # forward derivative
        return (f_right - f_c)/h
    
    if (not(type_right) and type_left):  # backward derivative
        return (f_c - f_left)/h
    
                                     
    return (f_right - f_left)/(2*h) # central derivative
    