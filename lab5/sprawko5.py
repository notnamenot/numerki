#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:00:11 2018

@author: ninja
"""

import math
import scipy
from scipy.linalg import solve_triangular
import numpy as np
from numpy.linalg import solve
from numpy.linalg import inv
from numpy.linalg import norm
from numpy.linalg import cond
from numpy.linalg import qr
from numpy.linalg import lstsq

print("Zad1\n")

A=np.array([[1,1],[1,1.0001]])
b1=np.array([2,2.0001])
b2=np.array([2,2])
x1=solve(A,b1)
x2=solve(A,b2)
print("x1 =",x1)
print("x2 =",x2)


Ainv = inv(A) #macierz odwrotna
#print(Ainv)

#W odróżnieniu od błędu zaokrągleń wprowadzonego przez algorytm, wskaźnik uwarunkowania stanowi informację o błędzie przeniesionym z danych. 
#Wskaźnik uwarunkowania macierzy definiuje się bardziej precyzyjnie jako maksymalny stosunek błędu względnego wektora rozwiązania x {\displaystyle x} x do błędu względnego b . {\displaystyle b.} b.
#Maksymalna wartość będzie iloczynem dwóch norm
#np.linalg.cond(A,2)
k=norm(A,2)*norm(Ainv,2) # współczynnik uwarunkowania
print("Współczynnik uwarunkowania: ",k)
print("Wraz z małą zmianą wektora prawych stron rozwiązanie znacznie się zmienia.")
print("Współczynnik uwarunkowania jest duży co świadczy o złym uwarunkowaniu układu.")

      
print("\nZad2\n")

def hil(i,j):
    return 1/(i+j+1)
def Hilbert(N):
     H=[]
     h=[]
     for k in range(N):
         h=[]
         for l in range(N):
             h.append(hil(k,l))
             #H[k][l]=hil(k,l)
         H.append(h)   
     return np.round(np.asarray(H),3)

N=8
H=Hilbert(N)
print("Macierz Hilberta:\n",H)

Hinv = inv(H)   #Compute the condition number of a matrix.
#k1a=cond(H,2)   #Compute the condition number of a matrix.
k1=norm(H,2)*norm(Hinv,2)#wskaznk uwarunkowania norma spektralna
k2=norm(H,np.inf)*norm(Hinv,np.inf)#wskaznk uwarunkowania norma wierszowa
k3=norm(H,1)*norm(Hinv,1)#wskaznk uwarunkowania norma kolumnowa
#norma  odwracalnej macierzy symetrycznej,  rzeczywistej jest równa najwi  ̨ekszemu modułowi spośród jej wartoścci własnych

#print(k1a)
print("\nWspółczynniki uwarunkowania macierzy korzystając z normy kolumnowej:",round(k3,2))
print("Współczynniki uwarunkowania macierzy korzystając z normy spektralnej:",round(k1,2))
print("Współczynniki uwarunkowania macierzy korzystając z normy wierszowej:",round(k2,2))
print("\nMacierz Hilberta jest źle uwarunkowana.")


print("\nzad3\n")

n=20
t = np.transpose(np.linspace(0,1,n))
b = [ math.cos(4*t[i]) for i in range(t.size) ]
b = np.transpose(b)

print(t)
print(b)

vand = np.vander(t,increasing=True)
#print(("\nMacierz Vand:\n {0}".format(vand)))
print(np.round(vand,3))
#print("\n",np.fliplr(np.round(vand,1)))


x1=solve(vand,b)
print("\n",np.round(x1,1))

q,r=qr(vand)     #A = QR of an orthogonal matrix Q and an upper triangular matrix R
x2=solve_triangular(r,b)
print("\n",np.round(x2,1))


m= lstsq(vand,b,rcond=None)[0]
x3=m
print("\n",x3)
#If a is square and of full rank then x (but for round-off error) is the exact solution of the equation

#norm1=b-vand*x1
#print(norm1)
 

