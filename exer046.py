"""
Faça um programa que receba um conjunto de valores inteiros e positivos, com o intervalo formado pelo número imprima na tela todos os números primos existentes  
"""

valor = 10

for i in range(2, valor):
    if(valor % i == 0):
       print("Não Primo")
       break
    print(valor)

