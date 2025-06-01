import numpy as np

def matM(i):
    """La fonction matM retourne une matrice 4-by-4
    """
    return np.array([[2*i+1, -5, 0, i],[-5, 3*i+2, -1, 3], [0, -1, 3*i-2, 1], [i, 3, 1, 7*i-3]])

def matN(n, i0, j0):
    """La fonction matN retourne une matrice n-by-n où n est un multiple de 4
    """
    N = np.zeros((n, n))
    for i in np.arange(0, n, 4):
        N[i:(i+4), i:(i+4)] = matM(i/4)
 
    # t sert pour l'indice de ligne pour traiter la colonne j0    
    if((j0+1)%4==0):
        t=j0//4
    else:
        t=(j0+1)//4
    N[(t+1)*4:,j0] = 6

    # t sert pour l'indice de colonne pour traiter la ligne i0    
    if((i0+1)%4==0):
        t=i0//4
    else:
        t=(i0+1)//4
    N[i0,(t+1)*4:] = 8
    return N

# tests sur matN
N0=matN(8, 1, 2)
N1=matN(12, 7, 4)
print(N0)
print(N1)
print(N1[7,:])
print(N1[:,4])
N2=matN(100, 12, 32)
print(N2[12,:])
print(N2[:,32])

#affichage des traces
print(np.trace(N0))  #11.0
print(np.trace(N1)) #39
print(np.trace(N2)) # 4450
