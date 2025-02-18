"""
Faça um programa que receba várias idades e que calcule e mostre a média das idades digitadas. Finalize digitando a idade igual a zero  
"""

soma_idades = 0
count = 0

while True:
    idade = int(input("Idade: "))

    if(idade <= 0):
        break

    soma_idades += idade
    count += 1

media_idade = soma_idades // count if count > 0 else 0

print(f"Media das Idades: {media_idade} anos")
