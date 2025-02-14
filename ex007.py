"""
Faça um programa que leia três números, verifique (usando if e else) e mostre o maior e o menor deles  
"""

x = float(input("Numero 1: "))
y = float(input("Numero 2: "))
z = float(input("Numero 3: "))

maior = x
menor = x

if y > maior:
    maior = y
if z > maior:
    maior = z

if y < menor:
    menor = y
if z < menor:
    menor = z

print(f"{maior} é o maior número")
print(f"{menor} é o menor número")    