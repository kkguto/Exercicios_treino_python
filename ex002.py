"""
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
"""

x = float(input("Digite um numero qualquer: "))

if x == 0:
    print(f"{x} é Nulo")
elif x > 0:
    print(f"{x} é Positivo")
else:
    print(f"{x} é Negativo")