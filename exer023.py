"""
Faça um programa que receba três inteiros e diga qual deles é o maior e qual o menor. Consegue criar mais de uma solução?  
"""

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))
z = int(input("Digite um numero: "))

maior = x
menor = x

if(y > maior):
    maior = y

if (z > maior):
    maior = z

if(y < menor):
    menor = y

if (z < menor):
    menor = z

print(maior, menor)