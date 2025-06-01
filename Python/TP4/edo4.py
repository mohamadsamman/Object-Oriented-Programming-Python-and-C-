# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy 


Y0 = np.array([1,0,1,-1])

n = 101
x = np.linspace(0, 4, n)
# fonction de l'EDO 2: dY/dt = f1(t, Y(t)) (2 composantes)
def f1(y,t):
    return np.array([y[1], y[2], y[3], 2*y[2]-y[1]-y[0]])
# appel a odeint
v1 = scipy.integrate.odeint(f1, Y0, x)
# affichage avec matplotlib (pas besoin des dérivées)
plt.plot(x, v1[:,0], 'o')
plt.xlabel('t')
plt.ylabel('y')

