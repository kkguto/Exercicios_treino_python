"""
Faça um programa que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos.
"""
maior_de_idade = 0

for i in range(10):
    print(f"Pessoa {i+1}")
    idade = int(input("Digite sua idade: "))

    if(idade >= 18):
        maior_de_idade+=1

print(f"\nTem {maior_de_idade} pessoas maiores de Idade\n")