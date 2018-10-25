"""
@Izabela Pachel
"""

import math
import numpy   #as np (alias)
import matplotlib.pyplot as plt

print("Zadanie 1\n")
k=1240*math.sqrt(7)
m=4467
l=2j        #liczba zespolona
d=k+m
c=d+l
#print(type(k))


# In[5]:


print("\nZadanie 2\n")
print(d)                    #domyślnie  
print(round(d,3))           #zaokrąglenie do 3 miejsc po przecinku
print(round(d,20))          #zaokrąglenie do 20 miejsc po przecinku


# In[6]:


print("\nZadanie 3\n")
r=17
h=33
S=2*math.pi*r*r+2*math.pi*r*h
print("Pole powierzchni walca wynosi: ",S)


# In[7]:


print("\nZadanie 5\n")
x=1
t=1
r=1
b=((x+r)/(r*math.sin(2*x)+3.3456))*x**(t-r)
print("Wynik: ", b)


# In[8]:


print("\nZadanie 6\n")
from numpy.linalg import inv
a=math.sqrt(2)
M=numpy.array([[a,1,-a],[0,1,1],[-a,a,1]])
Minv=inv(M)
Mtrans=numpy.transpose(M)
Mdet=numpy.linalg.det(M)

# a = np.matrix('1 2; 3 4')
#numpy.set_printoptions(precision=5)
#print(numpy.matrix(M))
print("Macierz M:\n {0}".format(M))
print("\nMacierz odwrotna:\n {0}".format(Minv))
print("\nMacierz transponowana:\n {0}".format(Mtrans))
print("\nWyznacznik macierz :\n {0}".format(Mdet))


# In[9]:


print("\nZadanie 7\n")
print("Element 1x1: {0}".format(M[0,0]))
print("Element 3x3: {0}".format(M[2,2]))
print("Element 3x2: {0}".format(M[2,1]))

w1=M[:,2]
w2=M[1,:]
print("Trzecia kolumna macierzy M: {0}".format(w1))
print("Drugi wiersz macierzy M: {0}".format(w2))


# In[25]:


print("\nZadanie 8\n")

    
coeffs=[1,-7,3,43,-28,-60]              #współczynniki
roots=numpy.roots(coeffs)               #roots of a polynomial = miejsca zerowe wielomiany

def spr(x):
    a = x**5-7*x**4+3*x**3+43*x**2-28*x-60  
    if (a != 0):
        print(x, " nie jest pierwiastkiem")
    else:
        print(x, " jest pierwiastkiem")

#print(roots) 

print("\n\nPierwiastki wielomianu: ")
for x in roots:
        print(x," ",end='')

print("\n\nsprawdzenie:")
       
for x in roots:
    spr(x)     
    
print("\nZaokrąglone pierwiastki wielomianu: ")
for x in roots:
        print(int(round(x))," ",end='')
        
print("\n\nsprawdzenie:")

for x in roots:
    spr(int(round(x))) 
        
#Niedokładnośc obliczeń wynika z tego, że nie wszystkie liczby da się reprezentować w systemie binarnym.


# In[12]:



print("\n\nZadanie 9\n")
#numpy.set_printoptions(precision=4); ciągi, przedziały
a1=numpy.arange(0.02,5.56,0.99) #(start,stop,step)
#mamy do czynienia z błędem reprezentacji. Ponieważ liczba 0.99 nie może być dokładnie przedstawiona w systemie. Przy każdym kroku powiększamy błąd.
print(a1)
a2=numpy.linspace(0.09,4.33,4)  #(start,stop,ile wyników)
print(a2)    
#podobnie jest tutaj, system nie jest w stanie dokladnie przedstawić wszystkich liczb 


# In[11]:


print("\nZadanie 10\n")
def f1(x):
    return x**3-3*x

x = numpy.linspace(-1,1)
y = numpy.linspace(-5,5)
z = numpy.linspace(0,5)
a = []
b = []
c = []
for i in x:
     a.append(f1(i)) 
for i in y:
     b.append(f1(i)) 
for i in z:
     c.append(f1(i)) 
     
plt.plot(y, b,'co',label='<-5,5>') 
plt.plot(z, c, 'r--',label='<0,5>') 
plt.plot(x, a,'k',label='<-1,1>')      #(przedział, punkty)
plt.title('Wykres funkcji')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#plt.axis([-5, 5, -125, 125])
plt.show()     


# In[3]:


print("\nZadanie 11\n")
m=2500    #g
v=60      #km/h
q=((m*0.001)*v**2*(10/36)**2)/2
print("Wynik w dżulach: ",round(q,3))
print("Wynik w kilokaloriach: ",round(q*0.0002388459,3))


m=3000
def f2(v):
        return (((m*0.001)*v**2*(10/36)**2)/2)
v = numpy.linspace(200,0)
u = f2(v)

plt.plot(v,u)
plt.title('Wykres zależności ilości ciepła wydzielonego \nw procesie hamowania od prędkości')
plt.xlabel('prędkość [km/h]')
plt.ylabel('ilość ciepła [J]')
plt.show() 

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.semilogy(v,u)           #Make a plot with log scaling on the y axis.
plt.title('Wykres zależności ilości ciepła wydzielonego \nw procesie hamowania od prędkości')
plt.xlabel('prędkość [km/h]')
plt.ylabel('ilość ciepła [J]')
#plt.yscale('log')
plt.xlim(0, 200)            #Get or set the x limits of the current axes.
plt.ylim(top=f2(200))
plt.show()

