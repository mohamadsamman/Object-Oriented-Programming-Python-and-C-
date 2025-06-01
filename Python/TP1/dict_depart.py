"""
Test sur un dictionnaire
"""
depart = {83 : "Var", 38 : "Isere", 26 : "Drome", 84 : "Vaucluse", 29 : "Finistere", 18 : "Cher", 12: "Aveyron", 60: "Oise", 33: "Gironde"}
print(depart)

L = list()  # L est une liste contenant les n°s de département < 30
for t in depart.keys():
    if(t<30):
        L.append(t)
L1 = list() # L1 contient les valeurs de depart pour les clés contenues dans L et ordonnées
L.sort()
for t in L:
    L1.append(depart[t])
    
print(L1)



L.clear()
for t in depart.keys():
    if(len(depart[t])>=6):
        L.append(t)
L.sort()
L1.clear()
for t in L:
    L1.append(depart[t])
    
print(L1)


L.clear()
L1.clear()
for t in depart.keys():
    if(len(depart[t])<=5):
        L.append(t)
L.sort()
for t in L[-1::-1]:
    L1.append(depart[t])
    
# alternative en utilisant l'option reverse=True de la méthode sort
# L.sort(reverse=True)
# for t in L:
#     L1.append(depart[t])
    
print(L1)


"""" Correction pour le cas où l'on considère les noms en "clés", et les numéros en "valeurs" """
# Méthode 1 : utiliser l'option key de la méthode sort
depart = { "Var" : 83 , "Isere" : 38,  "Drome" : 26 , "Vaucluse" : 84 ,  "Finistere" : 29 ,  "Cher" : 18 , "Aveyron" : 12, "Ain" : 1}
L=[]
for nom in depart.keys():
    if depart[nom]<30 :
        L.append(nom) # ou L=L+[nom]
L.sort(key=str.lower) #tri par ordre alphabétique (qui est le même que l'ordre des numéros de département)

# Méthode 2  Utiliser argsort sur un tableau numpy
import numpy as np
L=[] # contiendra les noms (=les clés)
L2=[] # contiendra les numeros (= les valeurs)
for nom in depart.keys():
    if depart[nom]<30 :
        L.append(nom)
        L2.append(depart[nom])

L=np.array(L)
L2=np.array(L2)
ordre=L2.argsort()
L=L[ordre]