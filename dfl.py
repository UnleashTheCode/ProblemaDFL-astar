from copy import deepcopy as cp
import numpy as np

class Nod():
    def __init__(self,stare,poz=0,h=0,suma=0):
        self.stare=stare
        self.suma=suma
        self.h=h
        self.poz=poz

n=int(input("Introduceti n="))
p=int(input("Introduceti p="))
q=int(input("Introduceti q="))

def testare(nodt,teritoriu,frontiera):
    for nod in frontiera:
        if np.array_equal(nod.stare,nodt.stare):
            return False
    for nod in teritoriu:
        if np.array_equal(nod.stare,nodt.stare):
            return False
    return True

def valid(stare,i,j):
    if i in stare:
        if j in stare:
            if 2*i in stare:
                if stare.index(i)<stare.index(j)<stare.index(2*i):
                    return True
    return False

def suma(nod):
    sum=0
    for i in range (len(nod.stare)-1):
        sum+=(nod.stare[i+1]-nod.stare[i])
    nod.suma=sum

stareI=[]
for i in range(n):
    stareI.append(0)

nodI=Nod(stareI,-1)
frontiera = []
teritoriu = []
frontiera.append(nodI)
solutie=Nod(stareI)
h=0
ok=True
x=nodI
nr=exnr=0

while ok==True:
    if len(frontiera) == 0:
        print("Insuccess")
        ok = False
        break
    while x.poz<n and ok==True:
        nodCurent=frontiera.pop(0)
        teritoriu.append(nodCurent)
        for i in range(1,n+1):
            x=cp(nodCurent)
            x.poz+=1
            nr+=1
            if(x.poz>n-1):
                ok=False
                break
            x.stare[x.poz]=i
            #print(x.stare)
            if testare(x,teritoriu,frontiera):
                frontiera.append(x)
            if valid(x.stare,p,q):
                suma(x)
                if(solutie.suma<x.suma):
                    solutie=cp(x)
                    #print(x.suma)
        if(nr>exnr):
            print("Functionez, dar gandesc mult.. Sunt la "+str(nr)+"-lea element.")
            exnr=nr+200
print("O solutie este: ",end='')
print(solutie.stare,end='')
print(" cu suma: ",end='')
print(solutie.suma)