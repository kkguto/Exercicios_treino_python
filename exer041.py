"""
Faça um programa que receba dez números e usando laços de repetição calcule e mostre a quantidade de números entre 30 e 90.  
"""

import random

quant = 0

for i in range(10):
    numero = random.randint(1, 100)

    if numero >= 30 and numero <= 90:
        quant += 1
        
        print(numero)

print(f"Quantidade de numeros: {quant}")