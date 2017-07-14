# -*- coding: utf-8 -*-
"""
Este programa imprime la sucesion de fibonacci
"""

def fibo(n):
    a,b = 0,1
    while b < n:
        print str(b) +" ",
        a,b = b, a+b

if __name__=='__main__':
    num = int(raw_input("Ingresa el numero de la sucesion: "))
    print "La serie es: "
    fibo(num)