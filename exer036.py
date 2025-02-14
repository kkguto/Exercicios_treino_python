"""
Faça um programa que recebe a altura de um triangulo em um número inteiro e imprima-o utilizando asteriscos. 

Veja o Exemplo:

Entrada: 5

*
**
***
****
*****
"""

n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()