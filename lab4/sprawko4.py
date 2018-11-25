#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:16:54 2018

@author: ninja
"""

#https://stackoverflow.com/questions/4003794/lagrange-interpolation-in-python

import math
import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
import scipy.misc
    

print("Zad1\n")

def my_interpolate_lagrange(x_values,y_values):
    def fun(x):
      sum = 0
      for i in range (len(x_values)):#??
          mul = 1
          for j in range (len(x_values)):
              if(i == j):
                  continue
              mul *= (x-x_values[j])/(x_values[i] - x_values[j])
          sum += y_values[i]*mul
      return sum   
    return fun
           
       



#https://www.johndcook.com/blog/2017/11/06/chebyshev-interpolation/
print("\nZad2\n")

def f(x):
    return 1/(25*x*x +1)

x0 = np.linspace(-2,2,200)
y0 = []
for i in range(x0.size):
    y0.append(f(x0[i]))
    
x = np.linspace(-2,2,21)
y = []
for i in range(x.size):
    y.append(f(x[i]))
   
    
n=21
xc=[]                   #węzły czebyszew
for k in range(1, n+1):
    xc.append(math.cos(math.pi*(2*k-1)/(2*n)))
#xc = [math.cos(math.pi*(2*k-1)/(2*n)) for k in range(1, n+1)]
for i in range(len(xc)):
   xc[i] = 2*xc[i]
xc=xc[::-1]
xch=np.array(xc)
ych=f(xch)
#print(xc)   
#print(ych)    

my_fun = my_interpolate_lagrange(x,y)
my_funch = my_interpolate_lagrange(xch,ych)

#interp1d = scipy.interpolate.interp1d(x0,y0)
#interp1dch = scipy.interpolate.interp1d(xch,ych)
#xnew = np.linspace(-2,2,21)
#ynew=interp1d(xnew)

#slpl = scipy.interpolate.splrep(x,y,s=0,k=3)
#slpl = scipy.interpolate.splrep(xch,ych,k=3)
spl = scipy.interpolate.InterpolatedUnivariateSpline(x, y,k=3)
splch = scipy.interpolate.InterpolatedUnivariateSpline(xch, ych,k=3)  

#scipy.interpolate.lagrange
#lg = scipy.interpolate.lagrange(x,y)

#polyfit = np.polyfit(x,y,3)    #Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y). 
#p = np.poly1d(polyfit)
#print(polyfit)

#poly1d = np.poly1d(np.polyfit(x, y, 21))#poly1d dostaje współczynniki i jest wielomianem


#chebroots=np.polynomial.chebyshev.chebroots(x)
#print(chebroots)
#chebfit=np.polynomial.chebyshev.chebfit(x,y,3) #Chebyshev coefficients ordered from low to high
#chebinterpolate=np.polynomial.chebyshev.Chebyshev.interpolate(f,3)
#print(chebfit)


plt.figure(num=None, figsize=(9, 7), dpi=80)
plt.plot(x0,f(x0), 'g-',label='f(x)')
plt.plot(x,f(x), 'co',label='węzły równoodległe')
plt.plot(xch,f(xch), 'ro',label='węzły Czebyszewa')
plt.plot(x,spl(x),'c--',label='m. funkcji sklejanych z węzłami równoodległymi')
plt.plot(xch,splch(xch),'r--',label='m.a funkcji sklejanychz węzłami czebyszewa')
plt.title('Interpolacja funkcjami sklejanymi',fontsize=18)
plt.xlabel('x',fontsize=14)
plt.ylabel('f(x)',fontsize=14)
plt.legend(loc='upper right',prop={'size': 8})
plt.show()



plt.figure(num=None, figsize=(9, 7), dpi=80)
plt.plot(x0,f(x0), 'g-',label='f(x)')
plt.plot(x,f(x), 'co',label='węzły równoodległe')
plt.plot(xch,f(xch), 'ro',label='węzły Czebyszewa')
plt.plot(x,my_fun(x),'c--',label='m. Lagrange\'a z węzłami równoodległymi')
plt.plot(xch,my_funch(xch),'r--',label='m. Lagrange\'a z węzłami czebyszewa')
plt.title('Interpolacja metodą Lagrange\'a',fontsize=18)
plt.xlabel('x',fontsize=14)
plt.ylabel('f(x)',fontsize=14)
plt.legend(loc='upper right',prop={'size': 9})
plt.show()


#interpolacja nie stosuje sie do wysokich rzedów; sklejanie albo aproksymacja
#interpolacja nie mówi co sie dzieje miedzy punktami


print("\nZad3\n")

x=[-10.0,-9.0,-8.0,-7.0,-6.0,-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
y=[-9.10,-8.82,-7.99,-7.10,-6.32,-5.33,-4.73,-3.65,-2.52,-1.28,0.00,1.26,2.49,3.61,4.61,5.51,6.32,7.10,7.81,8.45,9.02]

#scipy.interpolate.lagrange
lg = scipy.interpolate.lagrange(x,y)

interp1d = scipy.interpolate.interp1d(x,y,kind='linear')#interp1d zwraca funkcję interpolującą


polyfit1 = np.polyfit(x,y,deg=1)#polyfit dostaje współrzędne i stopień i zwraca wektor współczynników wielomianu
polyfit2 = np.polyfit(x,y,deg=2)
polyfit3 = np.polyfit(x,y,deg=3)
p1 = np.poly1d(polyfit1)#poly1d dostaje współczynniki wielomianu i zwraca wielomianem
p2 = np.poly1d(polyfit2)
p3 = np.poly1d(polyfit3)
#print(np.poly1d(p1))
#print(np.poly1d(p2))
#print(np.poly1d(p3))


plt.figure(num=None, figsize=(9, 7), dpi=80)
#plt.plot(x,y, 'y-',label='y(x)')
plt.plot(x,interp1d(x), 'k-',label='f. interpolująca')
plt.plot(x,p1(x), 'c-',label='ap. w. 1-go st.')
plt.plot(x,p2(x), 'g-',label='ap. w. 2-go st.')
plt.plot(x,p3(x), 'm-',label='ap. w. 3-go st.')
plt.title('Prędkość obrotowa silnika prądu stałego w zależności od napięcia jego zasilania',fontsize=12)
plt.xlabel('napięcie [V]',fontsize=14)
plt.ylabel('prędkość obrotowa [1000 RPM]',fontsize=14)
plt.legend(loc='lower right',prop={'size': 13})
#plt.grid(True, which="both")
plt.show()

print("\nAproksymacja wielomianem 3-go stopnia ma przebieg bardzo zbliżony do interpolacji wielomianowej.")


print("\nZad4\n")

t=[0.0,1.0,2.0,3.0]
s=[0.0,42.7,73.2,92.5]
x=79.6

interp1d = scipy.interpolate.interp1d(t,s)

polycoefs = np.polyfit(t,s,deg=3)
poly = np.poly1d(polycoefs)

polycoefs2 = np.polyfit(s,t,deg=3)
poly2 = np.poly1d(polycoefs2)
#print(np.poly1d(poly)) 
y=poly2(x)
#print(y)
print("Kierowca minął fotoradr po",round(y,2),"s." )

v = scipy.misc.derivative(poly,y)
#print(v)
v=v*3.6
print("Jechał z prędkością",round(v,2),"km/h.")

plt.figure(num=None, figsize=(6, 4), dpi=80)
plt.plot(t,poly(t), 'c-',label='położenie kierowcy w zależności od czasu')
#plt.plot(t,interp1d(t), 'r-',label='')
plt.plot(y,x,'ro',label='fotoradar')
plt.title('zależność położenia od czasu',fontsize=14)
plt.xlabel('czas [s]',fontsize=11)
plt.ylabel('położenie [m]',fontsize=11)
plt.legend(loc='lower right',prop={'size': 11})
plt.grid(True, which="both")
plt.show()