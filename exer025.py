"""
Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
"""

x = int(input("Digite um numero: "))

for i in range(1, 11):
    print(f"{i} x {x} = {i * x}")