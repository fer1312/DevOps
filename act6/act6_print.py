# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:40:01 2025

@author: mxfer
"""

print("Hola Fernanda, ingrese un número entero")

try:
    n = int(input())
    print("El numero ingresado es ", n)

    for number in range(n):
        print(number)
except:
    print("La entrada no es un entero")