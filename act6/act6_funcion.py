# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:35:51 2025

@author: mxfer
"""

def print_numbers():
    for number in range(n):
        if ((n % 2) == 0):
            print("El número ingresado es: ", number)
        else:
            print("El cuadrado del número es: ", pow(number,2))

print("Hola Fernanda, ingrese un número entero")
try:
    n = int(input())
    print("El numero ingresado es ", n)
    
    print_numbers()

except:
    print("La entrada no es un entero")
    
    