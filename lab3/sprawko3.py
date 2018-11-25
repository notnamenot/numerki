
# coding: utf-8

# In[264]:


"""
@author: Izabela Pachel
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import time

print("\nZadanie 1\n")

def f(x):                   
    return math.e**(-2*x)+x*x-1

def f1(x):
    return -2*math.e**(-2*x)+2*x

def f2(x):
    return 4*math.e**(-2*x)+2


v = np.linspace(-0.2,1.2)
p = f(v)
p1 = f1(v)
p2 = f2(v)

plt.figure(num=None, figsize=(9, 7), dpi=80)
plt.axhline(0, color='blue', lw=0.25)
plt.plot(v,p,label='f(x)')
plt.plot(v,p1,label='f\'(x)')
plt.plot(v,p2,label='f\'\'(x)')
plt.title('Wykres funkcji i jej pochodnych',fontsize=18)
plt.xlabel('x',fontsize=14)
plt.ylabel('f(x)',fontsize=14)
plt.legend(loc='upper right',prop={'size': 16})
plt.show()

print("\nNa podstawie wykresu możemy szacować, że pierwiastki równania f(x) = 0 mają wartości zbliżone do: 0 i 0.9.\n")

print("Przedziały dla metod bisekcji i siecznych: [-0.2,0.4], [0.5,1.0]")
print("Punkty startowe dla metody stycznych: -0.2, 0.5")


# In[265]:


print("\nZadanie 2\n")

stop = 10**-10 #Warunek zakończenia obliczeń: odległość pomiędzy kolejnymi przybliżeniami jest dość mała: |x_(k+1)-x_k|<=ep
maxit=100

def my_bisection(f,a,b,ep,n):
    c1=0
    c=(a+b)/2.0
    for i in range(n):
       if math.fabs(c - c1) <= ep:
           return c, i+1
       #if math.fabs(f(c)) <= ep:
       #    return c, i
       elif f(a)*f(c) < 0:
           b=c
       elif f(c)*f(b)<0:   
           a=c
       c1=c
       c=(a+b)/2.0 
       

print("Warunki wystarczające zbieżności metody bisekcji w przedziale [a,b] izolacji pierwiastka:\n")
print("\t1) Funkcja f(x) jest ciągła w przedziale dokniętym [a,b].")
print("\t2) Funkcja przyjmuje różne znaki na końcach przedziału (czyli zachodzi f(a)*f(b) < 0).")

print("\nMiejsca zerowe dla metody my_bisection:\n")

start = time.time()
bi1, it1 = my_bisection(f,-0.2,0.4,stop,100)
end = time.time()
bt1 = end-start
print("m0 =",bi1, "\tliczba iteracji =",it1, "\tczas działania =",bt1)

start = time.time()
bi2, it2 = my_bisection(f,0.5,1,stop,100)
end = time.time()
bt2 = end-start
print("m0 =",bi2, "\tliczba iteracji =",it2, "\tczas działania =",bt2)

print("\nMiejsca zerowe dla metody scipy.optimize.bisect:\n")

start = time.time()
bi3 = optimize.bisect(f,-0.2,0.4,xtol=stop,maxiter=maxit)
end = time.time()
bt3 = end-start
print("m0 =", bi3,"\t\t\t\tczas działania =",bt3)

start = time.time()
bi4 = optimize.bisect(f,0.5,1,xtol=stop,maxiter=maxit)
end = time.time()
bt4 = end-start
print("m0 =", bi4,"\t\t\t\tczas działania =",bt4)


# In[238]:


print("\nZadanie 3\n")

def my_newton(f,f1,x1,ep,n):   #stycznych
    x2 = 0
    for i in range(n):
        if math.fabs(x2-x1) <= ep:
            return x1, i+1
        x2 = x1
        x1 = x1-f(x1)/f1(x1)

print("Warunki wystarczające zbieżności metody stycznych dla ustalonego punktu startowego:\n")
print("\t1) Funkcja jest ciągła w przedziale domkniętym [a,b];")
print("\t2) Pierwsza i druga pochodna funkcji f(x) istnieją i są ciągłe w przedziale domkniętym [a,b].")#f(x) klasy C^2 
print("\t3) Na końcach przedziału [a,b] wartości funkcji f(x) przyjmują przeciwne znaki (czyli zachodzi f(a)*f(b) < 0).") 
print("\t4) Pierwsza i druga pochodna mają stały znak w całym przedziale [a,b] (w przedziale nie ma ekstremów lokalnych\t\t   i punktów przegięcia).")
print("\t5) W punkcie startowym funkcja f(x) przyjmuje ten sam znak co jej druga pochodna (czyli zachodzi f(x0)*f''(x0)>0)")

print("\nMiejsca zerowe dla metody my_newton:\n")

start = time.time()
newton1, it3 = my_newton(f,f1,-0.2,stop,100)
end = time.time()
nt1=end-start
print("m0 =",newton1, "\tliczba iteracji =",it3,"\tczas działania =",nt1)

start = time.time()
newton2, it4 = my_newton(f,f1,0.5,stop,100)
end = time.time()
nt2=end-start
print("m0 =",newton2, "\t\tliczba iteracji =",it4,"\tczas działania =",nt2)

print("\nMiejsca zerowe dla metody scipy.optimize.newton:\n")

start = time.time()
newton3 = optimize.newton(f,-0.2,fprime=f1,tol=stop,maxiter=maxit)
end = time.time()
nt3=end-start
print("m0 =",newton3,"\t\t\t\tczas działania =",nt3,)

start = time.time()
newton4 = optimize.newton(f,0.5,fprime=f1,tol=stop,maxiter=maxit)
end = time.time()
nt4=end-start
print("m0 =",newton4,"\t\t\t\t\tczas działania =",nt4)


# In[263]:


print("\nZadanie 4\n")

print("Warunki wystarczające zbieżności metody siecznych dla ustalonego punktu startowego:\n")
print("\t1) Funkcja jest ciągła w przedziale domkniętym [a,b];")
print("\t2) Pierwsza i druga pochodna funkcji f(x) istnieją i są ciągłe w przedziale domkniętym [a,b].")
print("\t3) Na końcach przedziału [a,b] wartości funkcji f(x) przyjmują przeciwne znaki (czyli zachodzi f(a)*f(b) < 0).") 
print("\t4) Pierwsza i druga pochodna mają stały znak w całym przedziale [a,b] (w przedziale nie ma ekstremów lokalnych\t\t   i punktów przegięcia).")

def my_secant(f,x1,x2,ep,n):
    tmp=0
    for i in range(n):
        if math.fabs(x1-x2) <= ep:
            return x2, i+1
        tmp=x2
        x2=x2-f(x2)*(x2-x1)/(f(x2)-f(x1))
        x1=tmp
        
print("\nMiejsca zerowe dla metody my_secant:\n")

start = time.time()
secant1, it5 = my_secant(f,-0.2,0.4,stop,100)
end = time.time()
st1=end-start
print("m0 =",secant1, "\tliczba iteracji =",it5,"\tczas działania =",st1)

start = time.time()
secant2, it6 = my_secant(f,0.5,1,stop,100)
end = time.time()
st2=end-start
print("m0 =",secant2, "\t\tliczba iteracji =",it6,"\tczas działania =",st2)
        
print("\nMiejsca zerowe dla metody scipy.optimize.newton (z użyciem secant):\n")

start = time.time()
secant3 = optimize.newton(f,-0.2,tol=stop,maxiter=maxit)
end = time.time()
st3 = end-start
print("m0 =",secant3,"\t\t\t\tczas działania =",st3)

start = time.time()
secant4 = optimize.newton(f,0.5,tol=stop,maxiter=maxit)
end = time.time()
st4 = end-start
print("m0 =",secant4,"\t\t\t\t\tczas działania =",st4,"\n\n")
  
nestedList=[["FUNKCJA","MIEJSCE ZEROWE","ITERACJI","CZAS OBLICZEŃ      [s]"],
            ["-"*15,"-"*23,"-"*9,"-"*22],
            ["my_bisection",str(bi1),str(it1),str(bt1)],
            ["bisection",str(bi3)," ",str(bt3)],
            ["my_newton",str(newton1),str(it3),str(nt1)],
            ["newton",str(newton3)," ",str(nt3)],
            ["my_secant",str(secant1),str(it5),str(st1)],
            ["secant",str(secant3)," ",str(st3)],
            ["-"*15,"-"*23,"-"*9,"-"*22],
            ["my_bisection",str(bi2),str(it2),str(bt2)],
            ["bisection",str(bi4)," ",str(bt4)],
            ["my_newton",str(newton2),str(it4),str(nt2)],
            ["newton",str(newton4)," ",str(nt4)],          
            ["my_secant",str(secant2),str(it6),str(st2)],           
            ["secant",str(secant4)," ",str(st4)],]

for item in nestedList:
    print("|",item[0]," "*(15-len(item[0])),"|",
         item[1]," "*(23-len(item[1])),"|",
         item[2]," "*(9-len(item[2])),"|",
         item[3]," "*(22-len(item[3])),"|",
        )


# In[ ]:





