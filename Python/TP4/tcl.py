# -*- coding: latin-1 -*-
"""
 Exo 3: Théorème Central Limite
"""
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

### Poisson mu=8
n =40 #100 #5000
# poisson
mu= 8
M = 2000 #3000
m = mu; sig=np.sqrt(mu)

# initialisation de TX
TX = np.zeros((n+1, M))

for k in range(M):
    v2= scipy.stats.poisson.rvs(mu, size=n)
    TX[0:n,k] = v2
    TX[n,k] = np.sum(v2)

nbins = 50
plt.hist(TX[n], bins=nbins, density=True)
x=np.linspace(min(TX[-1]),max(TX[-1]),100)
plt.plot(x, scipy.stats.norm.pdf(x, loc=n*m, scale=sig*np.sqrt(n)), 'r')

# pour verification
print('moyenne théorique=',n*mu, 'écart-type théorique=', sig*np.sqrt(n))
print('moyenne empirique=',np.mean(TX[-1]), 'écart-type empirique=', np.std(TX[-1]))


### Binomiale B(n1, p1): n1=30, p1=0.25
n1 = 30
p1 = 0.25
m =n1*p1; sig=np.sqrt(n1*p1*(1-p1))

# initialisation de TX
TX = np.zeros((n+1, M))

for k in range(M):
    v2= scipy.stats.binom.rvs(n1, p1, size=n, loc=0)
    TX[0:n,k] = v2
    TX[n,k] = np.sum(v2)

plt.figure()
nbins = 50
plt.hist(TX[n], bins=nbins, density=True)
x=np.linspace(min(TX[-1]),max(TX[-1]),100)
plt.plot(x, scipy.stats.norm.pdf(x, loc=n*m, scale=sig*np.sqrt(n)), 'r')
# pour verification
print('moyenne théorique=',n*m, 'écart-type théorique=', sig*np.sqrt(n))
print('moyenne empirique=',np.mean(TX[-1]), 'écart-type empirique=', np.std(TX[-1]))
