import numpy as np
import matplotlib.pyplot as plt

def g(lbda, n):
    v = np.zeros(n)
    f = lambda k: np.exp(-lbda)*lbda**k/np.math.factorial(k)

    for k in range(n):
        v[k] = f(k)
    return v
n = 25
M = np.zeros((n,3))
M[:,0] = g(11, n)
M[:,1] = g(7, n)
M[:,2] = g(5, n)
plt.figure()
plt.plot(np.arange(n),M[:,0],'d',color='r',ls='-')
plt.plot(np.arange(n),M[:,1],'o',color='g',ls='-')
plt.plot(np.arange(n),M[:,2],'*',color='k',ls='-')
plt.legend(['lambda=11','lambda=7','lambda=5'])
plt.xlabel('k',fontsize=15)
plt.ylabel('P',fontsize=15)
