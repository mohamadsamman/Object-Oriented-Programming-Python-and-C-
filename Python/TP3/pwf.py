import numpy as np
import matplotlib.pyplot as plt
class PWF:
    def __init__(self, y, v):
        self.y = y
        self.v = v
        self.taille = np.size(y)

    def __str__(self):
        a = "Fonction constante par morceaux de taille {0:d}, définie sur [{1:.3f}, {2:.3f}], de valeurs min {3:.3f} et max {4:.3f}".format(self.taille, min(self.y), max(self.y), min(self.v), max(self.v))
        return a

    def __mul__(self, alpha):
        res = np.array(self.v) * alpha
        return PWF(self.y, res)

    def __rmul__(self, alpha):
        res = np.array(self.v) * alpha
        return PWF(self.y, res)

    def plot(self, ls='-', color='b'):
        b = double_y(self.y)
        z = double_v(self.v)
        plt.plot(b, z, ls=ls, color=color)

    def integrate(self):
        I = 0.
        for i in np.arange(0, self.taille - 1):
            I += self.v[i]*(self.y[i+1] - self.y[i])
        return I
        
def double_y(y):
    n = np.size(y)
    if(n>1):
        w = np.zeros(2*n-2)
        w[0] = y[0]
        for i in np.arange(1, n-1):
            w[2*i-1] = y[i]
            w[2*i] = y[i]
        w[2*n-3] = y[n-1]
        return w

def double_v(v):
    n = np.size(v)
    if(n>1):
        z = np.zeros(2*n-2)
        z[0] = v[0]
        for i in np.arange(0, n-1):
            z[2*i] = v[i]
            z[2*i+1] = v[i]
        return z    
    
 
x = [0.1, 0.2, 0.7, 0.8]
val = [2, 1, -1, 0]
G = PWF(x, val)
print('Valeurs de G',  G.y, G.v, G.taille)


print(G)


G1 = G*6
G2 = -2*G
print(G1)
print(G2)


y = [0.2, 0.3, 0.6, 0.65, 0.8]
val = [-1, 2, -1, 4, 0]
Q = PWF(y, val)
print(Q.integrate())



G.plot()
#    plt.savefig('PB.eps')
plt.show(block=False)
#    plt.figure()
G2.plot(color='r')
plt.show(block=False)

print(Q)
plt.figure()
Q.plot(color='r')
plt.show(block=False)
