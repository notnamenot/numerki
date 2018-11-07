
# coding: utf-8

# In[106]:


"""
@author: Izabela Pachel
"""
import math
import numpy as np
import matplotlib.pyplot as plt


print("Zad 1\n")
p = math.pi     #dokładnie
p1 = 22/7       #przybliżenie
bb = math.fabs(p-p1)        #war bezwzględna
print("1a) Błąd bezwzględny: ", bb)
bw = bb/p
print("1b) Błąd względny:    ", bw)
   
p = math.exp(1)
p1 = 2.718
bb = math.fabs(p-p1)        #war bezwzględna
print("2a) Błąd bezwzględny: ", bb)
bw = bb/p
print("2b) Błąd względny:    ", bw)
   
p = math.pow(10,math.pi)
p1 = 1397
bb = math.fabs(p-p1)        #war bezwzględna
print("3a) Błąd bezwzględny: ", bb)
bw = bb/p
print("3b) Błąd względny:    ", bw)

"""
def silnia(n):              #iter, math.factorial()
    i=0
    suma=1
    while(n != i):
        i += 1
        suma = suma * i
    return suma
    """

p = math.factorial(9)   #silnia
p1 = math.sqrt(18*math.pi)*math.pow((9/math.exp(1)),9)

bb = math.fabs(p-p1)        #war bezwzględna
print("4a) Błąd bezwzględny: ", bb)
bw = bb/p
print("4b) Błąd zwzględny:   ", bw)
   


# In[110]:


print("\nZad 2\n")
#Metody numeryczne wykorzystywane są wówczas,gdy badany problem nie ma w ogóle rozwiązania analitycznego (danego wzorami) lub
#korzystanie z takich rozwiązań jest uciążliwe ze względu na ich złożoność.

#Rozwiązanie analityczne: Dokładny wynik numeryczny lub symboliczny (może wykorzystywać symbole,np. tan(83), pi, e).


def G_p(n):         #analitycznie nie, numerycznie tak!!!
    result = []

    for p in range(1,n+1):      #bo bez ostatniego
        G = (1.0/p)*(10**p * (1.0 + p*round(math.pi,15) * 10**-p) - 10**p)
        result.append(G)
    return(np.array(result))

#analityczne rozwiązanie sprowadz się do pi; nie zależy od p  

g = G_p(24)
pi = round(math.pi,15)
print("numerycznie:\n",g)
print("\nanalitycznie:\npi =",pi,"(nie zależy od p)")
#jak sumujemu od początku to błąd maleje maleje maleji i potem nie maleje; gorszy
#jak sumujemu od końca to bład dochodzi  do 0 ; lepszy wyniki

bb = []    
for i in range(len(g)):
    bb.append(round(math.fabs(g[i]-pi),15))        #war bezwzględna
print("\n2a) Błąd bezwzględny:\n", bb)

bw = []
for i in range(len(g)):
    bw.append(bb[i]/pi)   
print("\n2b) Błąd względny:\n", bw)


def fbb(n):
    h = (1.0/n)*(10**n * (1.0 + n*round(math.pi,15) * 10**-n) - 10**n)
    k = np.fabs(h-pi)
    return k




def fbw(n):
    h = (1.0/n)*(10**n * (1.0 + n*round(math.pi,15) * 10**-n) - 10**n)
    k = np.fabs(h-pi)/pi
    return k

#x = np.arange(1,24,1)          #od,do,co
x=np.linspace(1,24,24)              #od,do,ile
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.semilogy(x,fbb(x), 'ro',label='błąd bezwzględny') 
plt.semilogy(x,fbw(x), 'co',label='błąd względny')           #Make a plot with log scaling on the y axis. 
plt.title('Wykres zależności wartości błędów od wyrazu ciągu')
plt.xlabel('wyraz ciągu')
plt.ylabel('wartość błędu')
#plt.yscale('log')
plt.xlim(left = 0,right = 25)            #Get or set the x limits of the current axes.
plt.ylim()
plt.legend()
plt.show()
print("\nWraz ze zwiększaniem się wyrazów ciągu, logarytmicznie wzrasta wartość błędu, aż od pewnego momentu jest prawie stała. \nOznacza to, że algorytm jest numerycznie niepoprawny (obliczone rozwiązania przy nieco zaburzonych danych znacząco \nodbiegają od rozwiązania dokładnego).",end=" ")
print("Pojawia się błąd reprezentacji (występuje zaokrąglenie w przypadku liczby pi).") #Zaokrąglanie występuje w przypadku reprezentacji wszystkich liczb niewymiernych (tj. o nieskończonym rozwinięciu dwójkowym), takich jak np. π czy liczba Eulera.


# In[112]:


print("\nZad 3\n")

def sum_e(n):
    e = 0
    for i in range(0,n+1):
            e += 1/math.factorial(i)
    return e

e = math.exp(1)     
e1 = sum_e(5)
e2 = sum_e(10)

print("  dla n = 5:")
bb = math.fabs(e-e1)
print("1a) Błąd bezwzględny:", bb)
bw = bb/e
print("1b) Błąd względny:   ", bw)
print("  dla n = 10:")
bb = math.fabs(e-e2)
print("2a) Błąd bezwzględny:", bb)
bw = bb/e
print("2b) Błąd względny:   ", bw)

#aproksymacja czyli przybliżanie nieznanych funkcji 


# In[113]:


print("\nZad 4\n")

print(np.finfo(float))         #(float) The smallest representable positive number such that 1.0 + eps != 1.0. Type of eps is an appropriate floating point type.

a = 1.0
b = np.finfo(float).eps
print("smallest representable positive number:",np.finfo(b).eps)
print("a =",a)
print("b =",b)
print("a + b - a - b =",a+b-a-b)

"""
1 cyfra dziesiętna --- log2(10) bitów
x cyfr dziesiętnych --- 53 bity #u nas  precyzja: x = 16 cyfr dziesiętnych 

#liczba cyfr cechy określa zakres reprezentowalnych liczb
"""
m = 16 * math.log(10,2)#(x,base)
print("\nliczba bitów mantysy:",int(round(m,0)))
print("\nIlość bitów mantysy określa precyzję zapisu. Im jest większa, tym dokładniej można przedstawiać liczby rzeczywiste, ale ich reprezentacja w maszynie i tak wymaga skończonej długości słów binarnych, co prowadzi do błędu zaokrąglenia w trakcie wykonywania obliczeń.")



# In[117]:


print("\nZad 5\n")
"""
def sum_n(n):
    res = 0.0
    for i in range(1,n+1):
            res += 1/(i**2.0)
    return res

def pi(n):
    pi = math.sqrt(6.0*sum_n(n))
    return pi
"""
pi = lambda n : math.sqrt(6.0*sum([1/(i**2.0) for i in range(1,n+1)]))

print("Przybliżenia liczby pi dla:")
print("n = 1 :      ",pi(1))
print("n = 10 :     ",pi(10))
print("n = 100 :    ",pi(100))
print("n = 1000 :   ",pi(1000))
print("n = 10000 :  ",pi(10000))
print("n = 100000 : ",pi(100000))

print("\nMamy tu do czynienia z błędęm obcięcia, powstałym podczas obliczeń, na skutek zmniejszania liczby działań (podczas \nobliczania sum nieskończonych). Im większa ilość wyrazów jest uwzględniana, tym błąd obcięcia jest mniejszy i możemy \nznaleźć tym dokładniejszą wartość wyrażenia. Mamy też do czynienia z błędem zaokrąglenia powstałym na skutek konieczności \nzaokrąglania obliczonych wartości ze względu na ograniczoną długość słów binarnych.")

"""
Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. For example, 
the decimal fraction 0.125 has value 1/10 + 2/100 + 5/1000, and in the same way the binary fraction 0.001
Zagadnienie liczb zmiennoprzecinkowych (ang. floating point numbers - FP)

Liczby zmiennoprzecinkowe przechowują wartości przybliżone - pewnych liczb nie da się zapisać w systemie zmiennoprzecinkowym. Typowym przykładem są ułamki dziesiętne typu 1/10, 2/10,3/10. 
Takie ułamki posiadają nieskończone rozwinięcia w systemie dwójkowym, zatem wymagają mantys o nieskończonej ilości bitów, co nie jest możliwe do zrealizowania.
Ilość bitów mantysy określa precyzję zapisu. Im jest większa, tym dokładniej można przedstawiać liczby rzeczywiste - błędy zaokrągleń są mniejsze.
Ilość bitów cechy określa dopuszczalny zakres reprezentowanych liczb.

http://home.agh.edu.pl/~horzyk/lectures/pi/ahdydpiwykl2.html
https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.finfo.html
https://eduinf.waw.pl/inf/alg/006_bin/0021.php
https://eduinf.waw.pl/inf/alg/006_bin/0022.php
"""
