# -*- coding: utf-8 -*-
"""
  plotiris
  Affichage de nuage de points du jeu de données iris et histogrammes
"""

import matplotlib.pyplot as plt
import numpy as np
 
 
val = np.loadtxt('iris.txt')  # si le fichier est dans le répertoire, on l'importe

# calcul des moyennes, médianes et variance - mean, median utilisables sur des matrices
tmean = np.mean(val, 0)
tmedian = np.median(val, 0)
tvar = np.var(val, 0)

# liste des styles du plot
style = ['bo', 'rd', 'g*', 'k.']

#nb de bins
nbins = 20

t_one = np.ones(np.size(val,0))
for i in np.arange(np.size(val,1)):
    plt.figure()
    plt.plot(val[:,i], style[i])
    plt.plot(tmean[i]*t_one, 'y')
    plt.plot(tmedian[i]*t_one, 'm')
    plt.show(block=False)
    plt.show(block=False)
    
for i in np.arange(np.size(val,1)):
    plt.figure()
    plt.hist(val[:,i], nbins)
