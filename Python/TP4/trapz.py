# -*- coding: latin-1 -*-
"""
 Exo 4 du TP12: intégration numérique
"""
import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sin, cos, linspace, array, log

n = 1001; a  = 0; b =10
x = np.linspace(a, b, n) 
# définition de f
f = lambda x : exp(-x**2)*sin(3*x)-4*x*cos(x**2) +2

def my_trapz(f, a, b, n):
    """
     Fonction utilisant la méthode des trapezes
    """
    x = linspace(a, b, n)  # n points, (n-1) intervalles
    y = f(x)
    h = (b-a)/(n-1.) # pas de discretisation
    return h*(y[0]/2. + y[-1]/2. + np.sum(y[1:-1])) # utilisation de np.sum

# valeur de reference de l'integrale (attention, spi.quad renvoie aussi l'erreur numérique)
Iref = spi.quad(f, a, b)[0]
# affichage de my_trapz zt Iref
print(my_trapz(f,a,b,n), Iref)

# test de la fonction plot_erreur
th = 0.01*np.arange(1,11)
t1 = np.arange(1,11)
t2 = np.arange(1,11) + th**2

def plot_erreur(th, t1, t2):
    """
     Fonction plot_erreur: représente l'erreur |t1 - t2| en fonction de th
    """
    plt.loglog(th, abs(t1-t2),'-o')
    plt.xlabel('h')
    plt.ylabel('Erreur')
    plt.title('Erreur en fonction de h')
    p = (log(abs(t1-t2))[-1]-log(abs(t1-t2))[0])/(log(th)[-1]-log(th)[0])
    print('La pente est ', p)
    

plot_erreur(th, t1, t2)


# tableau des n
vn = array([51, 101, 1001, 5001, 10001, 50001, 100001])
# tableau des h (pas de discrétisation)
vh = array([])
# tableau des intégrales issues de my_trapz
v1 = array([])
for nn in vn:
    h = (b-a)/(nn-1.)    
    I = my_trapz(f, a, b, nn)
    vh = np.append(vh, h)
    v1 = np.append(v1, I)

# déf de v2 - contient toujours la même valeur
v2 = np.ones(len(v1))*Iref

# affichage de plot_erreur pour la methode des trapezes
plt.figure()
plot_erreur(vh, v1, v2)
