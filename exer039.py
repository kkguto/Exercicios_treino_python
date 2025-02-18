"""
Faça um programa que receba a idade e o peso de sete pessoas. Calcule e mostre:

A quantidade de pessoas com mais de 90 quilos;
A média das idades das sete pessoas;  
"""

quant_90quilos = 0
soma_idades = 0

for i in range(7):
    print(f"Pessoa {i+1}: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))

    soma_idades += idade

    if peso > 90:
        quant_90quilos += 1
    
media_idades = soma_idades / 7

print(f"A quantidade de pessoas com mais de 90 quilos: {quant_90quilos}")
print(f"A média das idades das sete pessoas: {media_idades}")