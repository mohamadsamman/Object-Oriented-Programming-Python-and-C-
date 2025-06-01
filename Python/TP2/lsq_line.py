# -*- coding: utf-8 -*-
"""
  lsq_line
  Méthode des moindres carrés et affichage
"""

import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt
x = np.array([1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
y = np.array([4.1, 26.4, 39.9, 56.5, 80.1, 112.2, 120.8, 138.0, 160.4, 167, 200.2])
n = np.size(x)



M = np.zeros((n,2))
M[:,0] = np.ones((n,1))[:,0] # Dans python, M[:,0] est unidimensionnel (taille 11), 
                            #tandis que np.ones((n,1)) est de taille (11,1), 
                            #donc dans un espace à deux dimensions, avec un seul élément 
                            #dans la première dimension. D'où le "[:,0]"
                            # On peut aussi faire M[:,0] = np.ones(n)
M[:,1] = x
gamma = solve(np.dot((M.T),M), np.dot((M.T),y.T))
#print(np.shape(gamma))
#print(gamma)
print('La droite des moindres carres a pour equation y = {1:f}*x + {0:f}'.format(gamma[0], gamma[1])) 

plt.plot(x, y, 'bo')
v = np.linspace(np.min(x), np.max(x), 21)
plt.plot(v, gamma[0] + v*gamma[1], label='droite ls')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y en fonction de x')
plt.legend()
plt.show(block=False)
plt.pause(5) # attends 5 secondes avant d'affiche la suite.


""" METHODE alternative : passer par le type np.matrix (produit matriciel avec A*B) """
M = np.matrix(np.zeros((n,2)))
M[:,0] = np.ones((n,1))
M[:,1] = np.matrix(x).T
gamma = solve((M.T)*M, (M.T)*np.matrix(y).T)
print('La droite des moindres carres a pour equation y = {1:f}*x + {0:f}'.format(gamma[0,0], gamma[1,0])) 

plt.plot(x, y, 'bo')
v = np.linspace(np.min(x), np.max(x), 21)
plt.plot(v, gamma[0,0] + v*gamma[1,0], label='droite ls')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y en fonction de x')
plt.legend()
plt.show(block=False)
plt.pause(5)
