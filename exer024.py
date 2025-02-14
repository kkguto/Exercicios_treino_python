"""
Crie um programa que peça um número ao usuário e armazene ele na variável x. Depois peça outro número e armazene na variável y. Mostre esses números. 
Em seguida, faça com que x passe a ter o valor de y, e que y passe a ter o valor de x.
"""

x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))

print(f"x = {x} e y = {y}")

x, y = y, x

print(f"x = {x} e y = {y}")
