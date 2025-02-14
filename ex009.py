"""Faça um programa que leia três números e mostre-os em ordem decrescente"""

x = int(input("Numero 1: "))
y = int(input("Numero 2: "))
z = int(input("Numero 3: "))

print(f"Ordem Inicial: {x, y, z}");

if (x < y):
    x, y = y, x;

if(y < z):
    y, z = z, y;

if (x < y):
    x, y = y, x;
    
print(f"Ordem Final: {x, y, z}");
