# -*- coding: utf-8 -*-
"""
  rectangle
  Maillage d'un rectangle avec des triangles et affichage
"""

import matplotlib.pyplot as plt
import numpy as np

def coord(nx, ny, h):
    """
     coord retourne la matrice des coordonnées
    """
    M = np.zeros(((nx+1)*(ny+1),2))
    indx = 0
    for i in np.arange(nx+1):
        for j in np.arange(ny+1):
            M[indx,0] = i*h
            M[indx,1] = j*h
            indx += 1
    return M

def connec(nx, ny):
    """
     connec retourne la matrice de connectivité
    """
    C = np.zeros((2*nx*ny,3),dtype=int)
    indx  = 0
    for i in np.arange(nx):
        for j  in np.arange(ny):
            C[indx,:] = np.array([i*(ny+1)+j,i*(ny+1)+j+1, i*(ny+1)+ny+2+j])
            indx += 1
            C[indx,:] = np.array([i*(ny+1)+j,i*(ny+1)+ny+j+1, i*(ny+1)+ny+2+j])
            indx += 1
    return C
            
def plot_triangle(M, t):
    """
     plot_triangle affiche un unique triangle avec matplotlib
    """
    v = np.array([M[t[0]][0], M[t[1]][0], M[t[2]][0], M[t[0]][0]])
    w = np.array([M[t[0]][1], M[t[1]][1], M[t[2]][1], M[t[0]][1]])
    plt.plot(v,w, 'k')
    return None

def plotmesh(nx, ny, h):
    """
     plotmesh affiche le maillage d'un rectangle de dimensions nx*h par ny*h
     et retourne les matrices des coordonnées et de connectivité
    """

    M = coord(nx, ny, h)
    C = connec(nx, ny)
    dim = np.shape(C)
#    print(dim[0])
    for i in np.arange(dim[0]):
        plot_triangle(M, C[i])

    plt.axis('equal')
    return M, C

plt.figure()
M, C = plotmesh(1, 1, 1)
plt.show(block=False)
#plt.pause(2)
plt.figure()
M, C = plotmesh(2, 2, 1.)
plt.show(block=False)
#plt.pause(2)
plt.figure()
plotmesh(8, 8, 1.)
plt.show(block=False)
#plt.pause(2)
plt.figure()
plotmesh(8, 10, 1.)
plt.show(block=False)
#plt.pause(2)
