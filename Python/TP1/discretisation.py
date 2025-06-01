# -*- coding: latin-1 -*-
import numpy as np
# Variable a
a = range(1, 31)
print('Variable a - De 1 à 30 par pas de 1')
for i in a:  #boucle for nécessaire si a est de type range. Inutile si on utilise arange ou linspace
    print(i)
# Variable b
b = np.arange(0, 101, 4)
print('Variable b - De 0 à 100 par pas de 4')
print(b)

# Variable c
c = np.arange(30, -1, -1)
print('Variable c - De 30 à 0 par pas de -1')
print(c)
# c = range(30, -1, -1) #alternative  
# for i in c:
#     print(i)
d = np.arange(1, 5.2, 0.2)
print('Variable d - De 1 à 5 par pas de 0.2')
print(d)


e = np.linspace(1,6,50)
print('Variable e - De 1 à 6 en 50 points')
print(e)
