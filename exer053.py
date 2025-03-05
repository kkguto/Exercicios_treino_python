"""
Faça um programa que receba várias idades e que calcule e mostre a média das idades digitadas. 
Finalize digitando idade igual a zero.  
"""

count = 0
soma_idade = 0

while True:
    print(f"\nPessoa {count+1}: ")
    idade = int(input("Idade: "))

    if idade <= 0:
        break

    soma_idade += idade
    count += 1

media = soma_idade // count

print(f"\nMedia das Idade: {media} anos")