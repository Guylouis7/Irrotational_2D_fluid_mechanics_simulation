#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""

def pressure(U, cl, dom, num, h):

    ## Constants:
    C = 0        # arbitrary fixed
    rho = 1000   # water density
    g = 9.81     # gravity acceleration
    
    return (rho * g * (C - 0 - (U**2 / (2*g))))  # we impose z = 0




    