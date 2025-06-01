# -*- coding: utf-8 -*-
"""
 Conversion de l'heure

 conv_heure(t)

 Input:  t: entier qui représente le temps en secondes
  Output: st: chaîne de caractères du type 'j jours, h heures, m minutes, s secondes' (avec les bonnes valeurs pour j, h, m, s)
"""
def conv_heure(t):
    print(" {0:d} secondes corresppondent à".format(t))
# nb de jours
    j = t//86400 # // -> division entière en python2 et python3; 86400 = 24*3600
# nb d'heures
    h = (t - (j*86400))//3600  # on retranche le temps des jours à t pour obtenir le nombre d'heures
# minutes
    m = (t - j*86400 - h*3600)//60 # on retranche le temps des jours et des heures à t pour obtenir le nombre de minutes
# secondes
    s = (t - j*86400 - h*3600 - 60*m) # on retranche le temps des jours, des heures et des minutes à t pour obtenir le nombre de secondes
    st = '{0:d} jours, {1:d} heures, {2:d} minutes et {3:d} secondes'.format(j, h, m, s)
    return st

print(conv_heure(3601))
print(conv_heure(17112))
print(conv_heure(3600))
print(conv_heure(12790))
print(conv_heure(63))
print(conv_heure(12))
print(conv_heure(9007))
print(conv_heure(156007))
