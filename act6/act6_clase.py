# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:01:48 2025

@author: mxfer
"""

class Entero:
    
    def __init__(self, n):
        self.n = n
        
    def print_numbers(self):
        for number in range(self.n):
            if ((self.n % 2) == 0):
                print("El número es: ", number)
            else:
                print("El cuadrado del número es: ", pow(number,2))
                
print("Hola Fernanda, ingrese un numero: ")
num = int(input())
E = Entero(num)
E.print_numbers()
