#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on  Mar 2025

@author: Leyen Benjamin Hendrickx Victor Lhoest Guy-Louis
"""

from section_plot import*
from velocity import velocity
from functools import partial
from pressure import pressure
from Lapl import laplacien
from circu import circu



def configuration1():
    h = 0.5

    dom = np.loadtxt('CL/1-dom.txt')


    num = np.loadtxt('CL/1-num.txt')


    cl = np.loadtxt('CL/1-cl.txt')

    
    
    U = velocity(h,cl,dom,num)[0]

    
    pressure_partial = partial(pressure, cl = cl, dom = dom, num = num, h = h)
    pressure_matrix = np.vectorize(pressure_partial)(U)
    section_plot(pressure_matrix, "Pressure", h,"Pa")


def compute_cl(dom, dom_bords, coord_obstacle, flow_percentage, h, J_CL_coef = 0.5):   

    cl = np.zeros_like(dom)

    Q_out = (10*7 + 5*9) * 10**(-3)
    node_number_out = 20 # the output is divided in 20 nodes
    L_out = node_number_out*h
    v_out = Q_out / L_out 
    

    psy_out = np.linspace(0, Q_out, 20)
    cl[1][1:21] = psy_out

    max_psy_out = psy_out[-1]
    psy_obstacle = J_CL_coef * max_psy_out

    for coord in coord_obstacle:
        cl[coord[0]][coord[1]] = psy_obstacle
    
   

    for i in range(dom_bords.shape[0]): 
        for j in range(dom_bords.shape[1]):
            if dom_bords[i,j] == 3:
                cl[i, j] = 0
            elif dom_bords[i,j] == 4:
                cl[i, j] = max_psy_out
            elif dom_bords[i,j] == 5:
                cl[i, j] = max_psy_out * (1-flow_percentage)
            elif dom_bords[i,j] == 0:
                cl[i, j] = np.nan
            elif dom_bords[i,j] == 1:
                cl[i, j] = np.nan

    
    psy_in_1 = np.linspace(cl[1][-2-19-1] , cl[1][-2], 21)
    cl[1][-2-19-1:-1] = psy_in_1

    psy_in_2 = np.linspace(cl[-2][-2-19-1] , cl[-2][-2], 21)
    cl[-2][-2-19-1:-1] = psy_in_2

    return cl
    
    


def configuration_obstacle(flow_percentage = 0.5, kutta_percentage = 0.5):
    h = 0.01

    dom = np.loadtxt('CL/2-dom.txt')

    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
    
    coord_obstacle= np.loadtxt('CL/2-contourObj.txt').astype(int)
    x_coord_obstacle = h*coord_obstacle[:,0]
    y_coord_obstacle = h*coord_obstacle[:,1]
    x_coord_obstacle_indices = coord_obstacle[:,0]
    y_coord_obstacle_indices = coord_obstacle[:,1]
    
    num = np.loadtxt('CL/2-num.txt')


    cl = compute_cl(dom, dom_bords, coord_obstacle, flow_percentage, h, kutta_percentage)

    section_plot(cl, r'Valeurs de $\psi$ aux conditions limites', h)

    
    velocity_matrices = velocity(h,cl,dom,num)
    U,u,v, psi = velocity_matrices
    
    section_plot(U, "Velocity", h,"m/s")
    vector_field(dom,velocity_matrices[1],velocity_matrices[2], psi, U, density=10)



    pressure_partial = partial(pressure, cl = cl, dom = dom, num = num, h = h)
    pressure_matrix = np.vectorize(pressure_partial)(U)
    section_plot(pressure_matrix, "Pressure", h,"Pa")
    u_circulation = u[x_coord_obstacle_indices, y_coord_obstacle_indices]
    v_circulation = v[x_coord_obstacle_indices, y_coord_obstacle_indices]
    circulation =  circu(v_circulation, u_circulation, x_coord_obstacle, y_coord_obstacle)


def velocity_plot():
    h = 0.01
    dom = np.loadtxt('CL/2-dom.txt')
    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
    
    coord_obstacle= np.loadtxt('CL/2-contourObj.txt').astype(int)
    num = np.loadtxt('CL/2-num.txt')

    
    cl1 = compute_cl(dom, dom_bords, coord_obstacle, 0.5, h)
    cl2 = compute_cl(dom, dom_bords, coord_obstacle, 0.7, h)
    rapport_Qin_Qout = ["0.5", "0.7"]
    
    fig, ax = plt.subplots(1, 2, figsize=(20, 20))

    for axes, cl,ratio in zip(ax, [cl1, cl2], rapport_Qin_Qout): 
        velocity_matrices = velocity(h, cl, dom, num)
        U, u, v, psi = velocity_matrices
        
        X, Y = np.meshgrid(np.arange(dom.shape[1]), np.arange(dom.shape[0]))
        
        axes.imshow(np.flip(np.flip(dom.T, None)) != 0, cmap='gray', 
                    extent=(0, dom.shape[1], 0, dom.shape[0]), alpha=0.4)
        
        axes.contour(np.flip(dom.T, 0), levels=[2], colors='black', linewidths=4, alpha=0.6)
        
        strm = axes.streamplot(X, Y, np.flip(v.T, 0), -np.flip(u.T, 0),
                            color=np.flip(U.T, 0), cmap='viridis',
                            density=3, linewidth=1.8, arrowsize=1.5)
        
        axes.invert_yaxis()
        fig.colorbar(strm.lines, ax=axes, label='Vitesse absolue (m/s)',shrink=0.8)
        
        axes.set_title(r'Vitesse pour '+ '$Q_{in,1}/Q_{out}$ =' + ratio)
        axes.set_xticks([])
        axes.set_yticks([])

    plt.tight_layout()
    plt.show()
    
def pressure_plot():
    h = 0.01
    dom = np.loadtxt('CL/2-dom.txt')
    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
    
    coord_obstacle= np.loadtxt('CL/2-contourObj.txt').astype(int)
    num = np.loadtxt('CL/2-num.txt')

    cl1 = compute_cl(dom, dom_bords, coord_obstacle, 0.5, h)
    cl2 = compute_cl(dom, dom_bords, coord_obstacle, 0.7, h)

    rapport_Qin_Qout = ["0.5", "0.7"]
    
    fig, ax = plt.subplots(1, 2, figsize=(20, 20))

    for axes, cl,ratio in zip(ax, [cl1, cl2], rapport_Qin_Qout):
        velocity_matrices = velocity(h, cl, dom, num)
        U, u, v, psi = velocity_matrices
        
        pressure_partial = partial(pressure, cl=cl, dom=dom, num=num, h=h)
        pressure_matrix = np.vectorize(pressure_partial)(U)
        
        # Affichage
        axes.imshow(np.flip(pressure_matrix.T, 0) != np.nan, cmap='gray', 
                    extent=(0, h * pressure_matrix.shape[1], 0, h * pressure_matrix.shape[0]), alpha=0.1)
        axes.imshow(np.flip(pressure_matrix.T, 0), cmap='plasma',
                    extent=(0, h * pressure_matrix.shape[1], 0, h * pressure_matrix.shape[0]), alpha=0.8)
        
        im = axes.imshow(np.flip(pressure_matrix.T, 0), cmap='plasma', 
                        extent=(0, h * pressure_matrix.shape[1], 0, h * pressure_matrix.shape[0]))
        
        axes.set_xticks([])
        axes.set_yticks([])
        axes.set_title(r'Pression pour '+'$Q_{in,1}/Q_{out}$ =' + ratio)
        fig.colorbar(im, ax=axes, label="Pression relative (Pa)", shrink=0.8)
        

    plt.tight_layout()
    plt.show()

def kutta_plot():
    h = 0.01
    dom = np.loadtxt('CL/2-dom.txt')
    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
    
    coord_obstacle= np.loadtxt('CL/2-contourObj.txt').astype(int)
    num = np.loadtxt('CL/2-num.txt')

    
    cl1 = compute_cl(dom, dom_bords, coord_obstacle, 0.5, h)
    cl2 = compute_cl(dom, dom_bords, coord_obstacle, 0.5, h, 0.13812529535243812)
    rapport_Qin_Qout = ["50", "~ 13.8"]  # voir valeur dans kutta_condition.py
    
    fig, ax = plt.subplots(1, 2, figsize=(20, 20))

    for axes, cl,ratio in zip(ax, [cl1, cl2], rapport_Qin_Qout): 
        velocity_matrices = velocity(h, cl, dom, num)
        U, u, v, psi = velocity_matrices
        
        X, Y = np.meshgrid(np.arange(dom.shape[1]), np.arange(dom.shape[0]))
        
        axes.imshow(np.flip(np.flip(dom.T, None)) != 0, cmap='gray', 
                    extent=(0, dom.shape[1], 0, dom.shape[0]), alpha=0.4)
        
        axes.contour(np.flip(dom.T, 0), levels=[2], colors='black', linewidths=4, alpha=0.6)
        
        strm = axes.streamplot(X, Y, np.flip(v.T, 0), -np.flip(u.T, 0),
                            color=np.flip(U.T, 0), cmap='viridis',
                            density=3.5, linewidth=1.2, arrowsize=1)
        
        axes.invert_yaxis()
        fig.colorbar(strm.lines, ax=axes, label='Vitesse absolue (m/s)',shrink=0.8)
        
        axes.set_title(r'Écoulement pour '+ ratio + ' %\ndu débit passant à droite de l\'obstacle\n' + r'($Q_{in,1}/Q_{out}$ = 0.5)')
        axes.set_xticks([])
        axes.set_yticks([])

    plt.tight_layout()
    plt.show()

def Cl_plot():
    h = 0.01

    dom = np.loadtxt('CL/2-dom.txt')

    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
   
    coord_obstacle= np.loadtxt('CL/2-contourObj.txt').astype(int)
    x_coord_obstacle = h*coord_obstacle[:,0]
    y_coord_obstacle = h*coord_obstacle[:,1]
    x_coord_obstacle_indices = coord_obstacle[:,0]
    y_coord_obstacle_indices = coord_obstacle[:,1]
   
    num = np.loadtxt('CL/2-num.txt')

    cl1 = compute_cl(dom, dom_bords, coord_obstacle, 0.5, h)
    cl2 = compute_cl(dom, dom_bords, coord_obstacle, 0.7, h)
    rapport_Qin_Qout = ["0.5", "0.7"]  
   
    fig, ax = plt.subplots(1, 2, figsize=(15, 30))

    for axes, cl,ratio in zip(ax, [cl1, cl2], rapport_Qin_Qout):
        axes.imshow(np.flip(cl.T, 0) != np.nan, cmap='gray',
                    extent=(0, h * cl.shape[1], 0, h * cl.shape[0]), alpha=0.1)
        axes.imshow(np.flip(cl.T, 0), cmap='plasma',
                    extent=(0, h * cl.shape[1], 0, h * cl.shape[0]), alpha=0.8)
       
        im = axes.imshow(np.flip(cl.T, 0), cmap='plasma',
                        extent=(0, h * cl.shape[1], 0, h * cl.shape[0]))

        axes.set_xticks([])
        axes.set_yticks([])
        axes.set_title(r'CL pour '+'$Q_{in,1}/Q_{out}$ =' + ratio)
       
        fig.colorbar(im, ax=axes, label="$\psi$", shrink=0.8)
   

    plt.tight_layout()
    plt.show()
    
def circu_reductible():
    h = 0.01

    dom = np.loadtxt('CL/2-dom.txt')

    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
    
    coord_reduct = np.array([[34,34,34,33,32,32,32,33,34],[3,4,5,5,5,4,3,3,3]]).T
    x_coord_reduct = h*coord_reduct[:,0]
    y_coord_reduct = h*coord_reduct[:,1]
    x_coord_reduct_indices = coord_reduct[:,0]
    y_coord_reduct_indices = coord_reduct[:,1]
    
    
    
    num = np.loadtxt('CL/2-num.txt')


    cl1 = compute_cl(dom, dom_bords, coord_reduct, 0.5, h)
    cl2 = compute_cl(dom, dom_bords, coord_reduct, 0.7, h)
    rapport_Qin_Qout = ["0.5", "0.7"]
    
    
    for cl in [cl1, cl2]:
        velocity_matrices = velocity(h, cl, dom, num)
        U, u, v, psi = velocity_matrices
        u_circulation = u[x_coord_reduct_indices, y_coord_reduct_indices]
        v_circulation = v[x_coord_reduct_indices, y_coord_reduct_indices]
        circulation =  circu(v_circulation.T, u_circulation.T, x_coord_reduct.T, y_coord_reduct.T)
        print ('circulation :', circulation)
        
def compute_circu_kutta():
    h = 0.01
    dom = np.loadtxt('CL/2-dom.txt')
    dom_bords = np.loadtxt('CL/2-dom_bords.txt')
    
    coord_obstacle= np.loadtxt('CL/2-contourObj.txt').astype(int)
    x_coord_obstacle = h*coord_obstacle[:,0]
    y_coord_obstacle = h*coord_obstacle[:,1]
    x_coord_obstacle_indices = coord_obstacle[:,0]
    y_coord_obstacle_indices = coord_obstacle[:,1]
    num = np.loadtxt('CL/2-num.txt')

    
    cl1 = compute_cl(dom, dom_bords, coord_obstacle, 0.5, h)
    cl2 = compute_cl(dom, dom_bords, coord_obstacle, 0.5, h, 0.13812529535243812)
    
    
    for cl in [cl1, cl2]:
        velocity_matrices = velocity(h, cl, dom, num)
        U,u,v, psi = velocity_matrices
        u_circulation = u[x_coord_obstacle_indices, y_coord_obstacle_indices]
        v_circulation = v[x_coord_obstacle_indices, y_coord_obstacle_indices]
        circulation =  circu(v_circulation.T, u_circulation.T, x_coord_obstacle.T, y_coord_obstacle.T)
        print ('circulation :', circulation)

if __name__ == "__main__":
    plt.rcParams.update({
        'font.size': 18,
        'axes.titlesize': 24,
        'axes.labelsize': 24,
        'legend.fontsize': 24,
        'xtick.labelsize': 22,
        'ytick.labelsize': 22,
        'figure.figsize': (20, 20),
    })
    #configuration1()
    #configuration_obstacle(flow_percentage=0.5,kutta_percentage=0.13812529535243812)

    #configuration_obstacle(flow_percentage=0.7)    
    velocity_plot()
    pressure_plot()
    kutta_plot()
    Cl_plot()
    compute_circu_kutta()