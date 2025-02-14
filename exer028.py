"""
Faça um programa que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + … + 1/n.
"""

n = int(input("Digite um numero inteiro: "))

s = 0.0

for i in range(1, n + 1):
    s += 1.0/i

print(s)