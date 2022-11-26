# calcul simple de la racine carrée
import random
import time
from decimal import Decimal
from math import sqrt


def milieu(a, b):
    return (a+b) / 2.0

def racineCarree(x: float) -> float:
    a = 0
    b = (1 if x<1 else x)
    mil = milieu(a,b)
    while mil*mil != x  and b != mil and a != mil :
        if mil*mil == x :
            return mil
        if mil*mil > x:
            b = mil
        else :
            a = mil
        mil = milieu(a,b)
        #print(str(a) + "  " + str(b) + " " + str(mil)+ " " + str(mil*mil))
    return mil

def racineCarree2(x):
    b = Decimal("0")
    increment = Decimal("1")
    while (b + increment) * (b + increment) != x and float(b) != float(b+increment) :
        #print(b, " ", b*b)
        while (b + increment) * (b + increment) > x :
            increment = increment / Decimal(10)
            #print("new increment " , increment)
        b = b + increment
    #print("carre " , b*b)
    return float(b)


def comparaison():
    mamethode = 0
    librairie = 0
    for i in range(1,1000):
        nombre = random.randint(1,10000)
        a = time.time()
        r1 = racineCarree(nombre)
        b = time.time()
        r2 = sqrt(nombre)
        c = time.time()
        mamethode += (b-a)
        librairie += (c-b)
        print (r1,"   ",r1*r1, "    ", r2, "    ", r2*r2)
    return (mamethode*1000, librairie*1000)


a, b = comparaison()
print("temps pour ma methode ",a, " temps librairie ", b, " ratio ", a/b)
#racineCarree2(2)
#racineCarree2(66)