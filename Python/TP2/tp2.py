import numpy as np
import matplotlib as plt
import math as m
#%% exo1

def Pois(lmbda,n):
    T=np.arange(0,n,1)
    for i in range(n):
        T[i]=(m.exp(-1*lmbda))*(lmbda**(i))/(m.factorial(i))
    return T

k=np.arange(0,25,1)
T11_25=np.array(Pois(11,25))
plt.plot(k,T11_25,color='red',marker='d')

T7_25=np.array(Pois(7,25))
plt.plot(k,T7_25,color='green',marker='o')

T5_25=np.array(Pois(5,25))
plt.plot(k,T5_25,color='black',marker='*')

plt.xlabel('k')
plt.ylabel('P')

#%% exo2
T=np.array(np.loadtxt(iris.txt))
x=np.linspace(0,151,1)
aff={0:'b',1:'r',2:'g',3:'k'}
aff2={0:'o',1:'d',2:'*',3:'.'}
truc1={0:'Sepal',1:'Sepal',2:'Petal',3:'Petal'}
truc2={0:'Length',1:'Width',2:'Length',3:'Width'}
for i in range (4):
    y=T[:,i]
    d=np.mean(y)
    m=np.median(y)
    plt.figure(i+1)
    plt.plot(x,y,color=aff[i],marker=aff2[i],xlabel=truc1[i],ylabel=truc2[i])
    plt.axhline(y=d, color='y', linestyle='-')
    plt.axhline(y=m, color='m', linestyle='-')

for i in range (4):
    y=T[:,i]
    plt.figure(i+1+4)
    plt.hist(y,20)

#%% exo3
def u(t,tm,ts):    
    u=(1/(1-ts/tm))*(m.exp((-t/tm)-m.exp(-t/ts)))
    return(u)

def uprime(t,tm,ts):  
    uprime=(1/(1-ts/tm))*((-1/tm)*m.exp((-t/tm)+(1/ts)*m.exp(-t/ts)))
    return(uprime)

X=np.linspace(0,13.01,0.01)
taum={0:0.1,1:1,2:1,3:1,4:1,5:1.1,6:2,7:4,}
taus={0:1,1:1.1,2:2,3:4,4:0.1,5:1,6:1,7:1}

for i in range(4):
    Y=np.array(u(X,taum[i],taus[i]))
    Yprime=np.array(uprime(taum[i],taus[i]))
    ymax=-5
    for j in range(len(Y)):
        if(Y[j]>ymax):
            ymax=Y[j]
    for i in range(1 ,9):
        plt.subplot(4 , 2 , i ) 
        plt.plot(X,Y,color='b')
        plt.plot(X,Yprime,color='orange')  
        plt.xlim(0,13)
        plt.ylim(-0.25,ymax)
        plt.title('tau_m= ',taum[i],' tau_s= ',taus[i] )
        plt.legend(fontsize=15)
        plt.tight_layout()
    
#%% exo4
xx=np.transpose(np.arange(0,55,5))
xx[0]=1
yy=np.transpose(np.array([4.1,26.4,39.9,56.5,80.1,112.2,120.8,138.0,160.4,167.,200.2]))
def droite(x,V):
    return(V[0]+x*V[1])
def lsq_line(x,y):
    plt.figure(666)
    plt.scatter(x,y)
    M=np.zeros((len(x),2))
    M[:,0]=1
    M[:,1]=x
    A=np.transpose(M)@M
    b=np.transpose(M)@y
    V=np.linalg.solve(A,b)
    abs=np.linespace(-5,5.01,0.01)
    ord=np.array(droite(abs))
    plt.plot(abs,ord)
    plt.legend()
    return(0)
lsq_line(xx,yy)