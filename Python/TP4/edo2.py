"""
 Exo 1: EDO du 1er et 2nd ordre
"""
import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

# fonction de l'EDO 1: dy/dt = f(t, y(t))
def f(y,t):
    return (t+4)/2.*np.exp(3*t/2.)+3*y/2.
# Condition Initiale EDO 1 (numpy array ou scalaire ou liste)
y0 = np.array([-5])
# discretisation de [0,3]
n = 21
x = np.linspace(0, 3, n)
# appel à odeint
v = scipy.integrate.odeint(f, y0, x)
# solution exacte de l'EDO1
def uex(t):
    return ((1/4.)*t**2+2*t-5)*np.exp(3*t/2.)
# affichage avec matplotlib
plt.plot(x, v, 'o')
plt.plot(x, uex(x))
plt.xlabel('t')
plt.ylabel('u')
plt.show(block=False)
#
#
plt.figure()
# Condition Initiale EDO 2 (numpy array ou liste)
Y0 = np.array([2,-1])
# discretisation de [0,2]
n = 21
x = np.linspace(0, 2, n)
# fonction de l'EDO 2: dY/dt = f1(t, Y(t)) (2 composantes)
def f1(y,t):
    return np.array([y[1], 4*y[0]])
# appel a odeint
v1 = scipy.integrate.odeint(f1, Y0, x)
# solution exacte de l'EDO 2
def yex(t):
    return 3/4.*np.exp(2*t)+5/4.*np.exp(-2*t)
# affichage avec matplotlib (pas besoin de la dérivée)
plt.plot(x, v1[:,0], 'o')
plt.plot(x, yex(x))
plt.xlabel('t')
plt.ylabel('y')
plt.show(block=False)
