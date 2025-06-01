# -*- coding: utf-8 -*-
#
# Calcul des racines réelles d'un polynôme de degré 2 avec affichage des solutions éventuelles
#
# solve2(lc)
#
# Input:  lc: liste contenant les coefficients du polynôme. Par ex: lc = [5, 6, -2] correspond au polynôme 5*x**2 + 6*x -2
# Output: s: tableau numpy contenant les racines du polynôme (vide si pas de solution)

# compute_sol renvoie un tableau numpy contenant les racines réelles éventuelles du polynôme
def compute_sol(lc):
    from numpy import sqrt, array
    discr = lc[1]**2 - 4*lc[0]*lc[2]  # discriminant
    eps = 1e-8    # test de précision numérique
    if (abs(lc[0])>eps):  # on teste si lc[0] différent de 0
        if(discr>0):
            return (array([-1,1])*sqrt(discr) -lc[1])/(2.*lc[0])  # tableau numpy à deux éléments
        else:
            if(discr==0):
                return array([-lc[1]/(2.*lc[0])])
            else:
                return array([])
    elif (abs(lc[1])>eps):     # on teste si lc[1] différent de 0
        return array([-lc[2]/lc[1]])
    else:
        print('Le polynôme est un polynôme constant! Pas de racine renvoyée')
        return array([])

# solve2 fit appel à compute_sol et gère l'affichage de solutions ou pas
def solve2(lc):
    s = compute_sol(lc)
    a = lc[0]; b = lc[1]; c = lc[2]
    eps = 1e-8    # test de précision numérique
    if (len(s)==2):
        print('Les racines du polynome ({0:d}*x^2) + ({1:d}*x) + ({2:d}) sont {3:f} et {4:f}'.format(a, b, c, s[0], s[1]))
    elif (len(s)==1):
        if (abs(a)>eps):  # on teste si a est différent de 0
            print('La racine double du polynome ({0:d}*x^2) + ({1:d}*x) + ({2:d}) est {3:f}'.format(a, b, c, s[0]))    
        else:
            print('La racine du polynome ({1:d}*x) + ({2:d}) est {3:f}'.format(a, b, c, s[0]))    
    else:
        print('Pas de racine reelle pour le polynome ({0:d}*x^2) + ({1:d}*x) + ({2:d})'.format(a, b, c))
    return s
        

s1 = solve2([1, -4, 3])
s2 = solve2([1,0,1])
s3 = solve2([1,2,1])
solve2([1, -4, -12])  # (-2, 6)
solve2([3, -13, 4])   # (1/3., 4)
solve2([0, 5, 1])   # (-1/5.)
solve2([0, 0, 7])
