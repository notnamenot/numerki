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
from scipy.interpolate import lagrange
from scipy.interpolate import interp1d
    

print("Zad1\n")

def my_interpolate_lagrange(x_values,y_values):
    assert len(x) == len(y) != 0
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
y0 = [ f(x0[i]) for i in range(x0.size) ]

    
x = np.linspace(-2,2,21)
y = [ f(x[i]) for i in range(x.size) ]
  
    
n=21

#xc=[]                   #węzły czebyszew
#for k in range(1, n+1):
#    xc.append(math.cos(math.pi*(2*k-1)/(2*n)))
xc = [ 2*math.cos(math.pi*(2*k-1)/(2*n)) for k in range(1, n+1) ] #węzły czebyszewa
    
#for i in range(len(xc)):#dostosowanie do przedziału
#   xc[i] = 2*xc[i]      
xc=xc[::-1]
xch=np.array(xc)
ych=f(xch)


plt.figure(num=None, figsize=(12, 8), dpi=80)
plt.plot(x0,y0, linestyle='-',linewidth=0.5, color='black', label='y=f(x)')
plt.plot(x,f(x), 'co',label='węzły równoodległe')
plt.plot(xch,f(xch), 'ro',label='węzły Czebyszewa')
plt.plot(x0,lagrange(x,y)(x0),'c-',label='m. Lagrange\'a z węzłami równoodległymi')
plt.plot(x0,lagrange(xch,ych)(x0),'r-',label='m. Lagrange\'a z węzłami czebyszewa')
plt.title('Interpolacja metodą Lagrange\'a',fontsize=18)
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.ylim(bottom=-0.4,top=1.1)
plt.legend(loc='upper right',prop={'size': 10})
#plt.grid()
plt.show()




plt.figure(num=None, figsize=(12, 8), dpi=80)
plt.plot(x0,y0, linestyle='-',linewidth=0.5, color='black',label='y=f(x)')
plt.plot(x,y, 'co',label='węzły równoodległe')
plt.plot(xch,ych, 'ro',label='węzły Czebyszewa')
plt.plot(x0,interp1d(x,y,'cubic')(x0),'c-',label='m. funkcji sklejanych z węzłami równoodległymi')
plt.plot(x0,interp1d(xch,ych,'cubic',bounds_error=False)(x0),'r-',label='m. funkcji sklejanychz węzłami czebyszewa')
plt.title('Interpolacja metodą funkcji sklejanych',fontsize=18)
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.ylim(bottom=-0.2,top=1.1)
plt.legend(loc='upper right',prop={'size': 9})
plt.show()


#interpolacja nie stosuje sie do wysokich rzedów; sklejanie albo aproksymacja
#interpolacja nie mówi co sie dzieje miedzy punktami
print("W przypadku węzłów równoodległych mamy do czynienia z \"efektem Rungego\". Początkowo ze wzrostem liczby węzłów przybliżenie poprawia się, jednak po dalszym wzroście zaczyna się pogarszać, co jest szczególnie widoczne na końcach przedziału." )
print("Takie zachowanie wielomianu interpolującego jest zjawiskiem typowym dla interpolacji za pomocą wielomianów wysokich stopni przy stałych odległościach węzłów.")
print("Aby uniknąć tego efektu, stosuje się interpolację z węzłami coraz gęściej upakowanymi na krańcach przedziału interpolacji - węzłami Czebyszewa.")


print("\nZad3\n")

x0 = np.linspace(-20,20,200)


x=np.arange(-10,11,1)
#x=np.array(x)
#x=np.linspace(-10,10,21)
#x=[-10.0,-9.0,-8.0,-7.0,-6.0,-5.0,-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
y=[-9.10,-8.82,-7.99,-7.10,-6.32,-5.33,-4.73,-3.65,-2.52,-1.28,0.00,1.26,2.49,3.61,4.61,5.51,6.32,7.10,7.81,8.45,9.02]



polyfit1 = np.polyfit(x,y,deg=1)    #polyfit dostaje współrzędne i stopień i zwraca wektor współczynników wielomianu
polyfit2 = np.polyfit(x,y,deg=2)
polyfit3 = np.polyfit(x,y,deg=3)
p1 = np.poly1d(polyfit1)            #poly1d dostaje współczynniki wielomianu i zwraca wielomian
p2 = np.poly1d(polyfit2)
p3 = np.poly1d(polyfit3)
#print(np.poly1d(p1))
#print(np.poly1d(p2))
#print(np.poly1d(p3))


plt.figure(num=None, figsize=(9, 7), dpi=80)
#plt.plot(x0,scipy.interpolate.interp1d(x,y,kind="cubic",bounds_error=False,fill_value="extrapolate")(x0), 'k-',label='f. interpolująca')
plt.plot(x,y,'ro',label='zadane węzły')
plt.plot(x0,lagrange(x,y)(x0), 'k-',label='f. interpolująca')
plt.plot(x0,p1(x0), 'c-',label='apr. w. 1-go st.')
plt.plot(x0,p2(x0), 'g-',label='apr. w. 2-go st.')
plt.plot(x0,p3(x0), 'm-',label='apr. w. 3-go st.')
plt.title('Prędkość obrotowa silnika prądu stałego w zależności od napięcia jego zasilania',fontsize=12)
plt.xlabel('napięcie [V]',fontsize=14)
plt.ylabel('prędkość obrotowa [1000 RPM]',fontsize=14)
plt.ylim(bottom=-15,top=15)
plt.legend(loc='lower right',prop={'size': 13})
#plt.grid(True, which="both")
plt.show()

print("\nW przypadku interpolacji wielomianowej mamy do czynienia z efekten Rungego - wartości pomiędzy węzłami na krańcach przedziału są odległe od oczekiwanych.")
print("Dlatego lepiej jest użyć aproksymacji wielomianami. Na zadanym przedziale [-10,10] najlepiej sprawdza się wielomian 3-go stopnia, ale wielomiany pozostałych stopni lepiej aproksymują zakres rozszerzony.")



print("\nZad4\n")

t0 = np.linspace(0,3,200)

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
print("Kierowca minął fotoradr po",round(y,2),"s." )

v = scipy.misc.derivative(poly,y)
#print(v)
v=v*3.6
print("Jechał z prędkością",round(v,2),"km/h.")

plt.figure(num=None, figsize=(6, 4), dpi=80)
plt.plot(t0,poly(t0), 'c-',label='położenie kierowcy w zależności od czasu')
#plt.plot(t,interp1d(t), 'r-',label='')
plt.plot(y,x,'ro',label='położenie fotoradaru')
plt.title('zależność położenia od czasu',fontsize=14)
plt.xlabel('czas [s]',fontsize=11)
plt.ylabel('położenie [m]',fontsize=11)
plt.legend(loc='lower right',prop={'size': 11})
plt.grid(True, which="both")
plt.show()