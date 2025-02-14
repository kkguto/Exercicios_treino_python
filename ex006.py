"""
Faça um programa que leia três números, verifique (usando if e else), e mostre o maior deles. 
"""

x = float(input("Numero 1: "))
y = float(input("Numero 2: "))
z = float(input("Numero 3: "))

if x > y and x > z:
    print(f"{x} é maior número")
elif y > x and y > z:
    print(f"{y} é maior número")
else:
    print(f"{z} é maior número")