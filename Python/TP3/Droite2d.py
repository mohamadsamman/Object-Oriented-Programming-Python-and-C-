from numpy import array, linspace
from numpy.linalg import norm
import matplotlib.pyplot as plt
import numpy as np

class Droite2d:
    """Classe Droite2d: un point en 2D
    """
    def __init__(self, v=np.zeros(2), style="-", color="b"):
        self.v = v
        self.style = style
        self.color = color

    def __eq__(self, d):
        eps = 1e-8
        if norm(self.v - d.v, np.inf)<eps:
            return True
        else:
            return False

    def plot(self):
#        x = linspace(-10, 10)
        x = np.array([-10, 10])
        y = self.v[0]*x + self.v[1]
        plt.plot(x, y, self.color, ls=self.style)
    def intersect(self,d): # /!\ l'énoncé n'est pas clair. On peut définir une méthode de la classe ou une fonction (extérieure à la classe, voir plus bas)
        eps=1e-8
        if abs(self.v[0]-d.v[0])>eps:
            return array([(self.v[1]-d.v[1])/(d.v[0]-self.v[0]),(self.v[1]*d.v[0]-d.v[1]*self.v[0])/(d.v[0]-self.v[0])])
        else:
            print('pas d''intersection ou droites confondues')
            return array([])
        
    def __str__(self):
        return("Droite d'équation y = {0:.2f}*x + {1:.2f}\n".format(self.v[0], self.v[1]))

def intersect(d1, d2): 
    eps = 1e-8
    if(abs(d1.v[0] - d2.v[0])> eps):
        return array([(d1.v[1]-d2.v[1])/(d2.v[0]-d1.v[0]),(d1.v[1]*d2.v[0]-d2.v[1]*d1.v[0])/(d2.v[0]-d1.v[0])])
    else:
        print('pas d''intersection ou droites confondues')
        return array([])
if __name__ == "__main__": # n'est pas executé si Droite2d.py est importé par un autre script
    d0 = Droite2d()
    d1 = Droite2d(np.array([1, 1]), ':', 'k')
    d2 = Droite2d(np.array([2, -1]), '--', 'g')    
    d3 = Droite2d(np.array([4, 2]), '-')    
    print(d0, d1, d2)
    plt.figure()
    d0.plot()
#    plt.xlim((-10, 10))
#    plt.show(block=False)
#    plt.figure()
    d1.plot()
#    plt.xlim((-10, 10))
#    plt.axis('equal')
#    plt.show(block=False)
#    plt.figure()
    d2.plot()
    plt.xlim((-10, 10))
#    plt.axis('equal')
    plt.show(block=False)
    print(intersect(d1, d2)) # même résultat que d1.intersect(d2)
    print(intersect(d1, d3)) # même résultat que d1.intersect(d3)
    print(intersect(d2, d3)) # même résultat que d2.intersect(d3)
    print(d1==d3)
    print(d1==d1)
    l = Droite2d(np.array([-2, 1]), style=":", color="r")
    print(l)
    I = intersect(d1, d2)
    print('Intersection d1 d2 = [{0:.2f},{1:.2f}]'.format(I[0], I[1]))



