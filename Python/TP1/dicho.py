# -*- coding: utf-8 -*-
#
# Dichotomie
#
# dicho(f, a, b, kmax=20)
#
# Input:  f: fonction mathématique pour laquelle on cherche un zéro
# Input: a: réel de l'intervalle [a,b]
# Input: b: réel de l'intervalle [a,b]
# Input: kmax: nbre maximum d'itérations (kmax=20, par défaut)


def dicho(f, a, b, kmax=50):
    eps = 1e-8
    deb, fin, x = a, b, (a + b)/2.
    for i in range(kmax):
        if (abs(f(x))<=eps):
            break
        if (f(fin)*f(x)<0.):
            deb = x
        else:
            fin = x
        x = (deb + fin)/2.
    return x

from math import sin, sqrt
g = lambda x: sqrt(1+x**3) - 7 # définition de la 1re fonction
x = dicho(g, -1, 50)
print('sqrt(1+x**3) - 7')
print([x, g(x)])   # vérification de g(x) (doit être proche de 0!)

f = lambda x: x**2-6*x*sin(2*x) + 2  # définition de f
x = dicho(f, -20, -4)
print('\n')
print('x**2-6*x*sin(2*x) + 2')
print([x, f(x)]) # vérification de f(x) (doit être proche de 0!)
x = dicho(f, -20, -4, kmax=75)  # on change kmax
print([x, f(x)])   
x = dicho(f, -20, 0, kmax=75)  # on change l'intervalle [a,b]
print([x, f(x)])
