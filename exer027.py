"""
Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzam resto igual a 2.
"""

for i in range(1000, 2001):
    if(i % 11 == 2):
        print(i)