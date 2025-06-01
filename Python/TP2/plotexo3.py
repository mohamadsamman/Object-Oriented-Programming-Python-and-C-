# -*- coding: utf-8 -*-
"""
  plotexo3
  subplot pour 8 fonctions (et sa dérivée) différentes
"""

from numpy import exp, arange
import matplotlib.pyplot as plt

# u est une fonction qui définit une fonction
def u(taum, taus):
    g = lambda t: 1./(1 - taus/taum)*(exp(-t/taum) - exp(-t/taus))
    return g

# du est une fonction qui définit une fonction
def du(taum, taus):
    g = lambda t: 1./(1 - taus/taum)*(-1./taum*exp(-t/taum) +1./taus*exp(-t/taus))
    return g

xmax = 13
ymin = -0.25
pas = 0.1  # pas de discrétisation
l = [[0.1, 1], [1, 1.1], [1, 2], [1, 4], [1, 0.1], [1.1, 1], [2, 1], [4, 1]]

vx = arange(xmax, step=pas)  # de 0 à xmax-pas
lmax = []
cpt = 1 # compteur pour subplot

# calcul du max avec la liste lmax
for vt in l:
    f = u(vt[0], vt[1])
    vy = f(vx)
    lmax.append(max(vy))    

# subplot
for vt in l:
    plt.subplot(4, 2, cpt) #4 lignes, 2 colonnes, le tracé se fait dans le compartiment numéro cpt
    cpt += 1
    f = u(vt[0], vt[1])
    df = du(vt[0], vt[1])
    vy = f(vx)
    plt.plot(vx, f(vx), '-o', markersize=1, label='u')
    plt.plot(vx, df(vx), '-o', markersize=1,label='du/dt')   
    plt.axis([0, xmax, ymin, max(lmax)])
    plt.title('tau_m={0:.1f}, tau_s={1:.1f}'.format(vt[0],vt[1]))
    plt.legend(fontsize=10,loc=1)  
plt.tight_layout()

 
