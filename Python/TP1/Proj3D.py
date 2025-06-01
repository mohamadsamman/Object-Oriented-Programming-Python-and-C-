import numpy as np
def Proj3D(u,v,w):
    Q=np.zeros((3,3)) #  
    Q[:,0]=u ; Q[:,1]=v ; Q[:,2]=w #matrice de passage de la base canonique à (u,v,w)
    #Q=np.stack((u,v,w),axis=1) # alternative
    # D est incluse dans P ssi la famille (u,v,w) est liée ss det(Q)=0
    if abs(np.linalg.det(Q))<1e-8: #marge d'erreur liée aux possibles arrondis lors du calcul de det(Q) 
        print("D est incluse dans P : projection mal définie")
        return
    else : 
        A=np.array([[1,0,0],[0,1,0],[0,0,0]]) # matrice de projection dans la base u,v,w
        M=Q@A@np.linalg.inv(Q)
        return M
    

u=np.array([1,0,1])
v=np.array([0,1,-1])
w=np.array([1,-1,1])
print(Proj3D(u,v,w))
        