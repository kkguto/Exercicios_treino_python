"""
Faça um programa que receba dez idades, pesos e Alturas e que calcule e mostre:

A média das idades das dez pessoas;
A quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50;
A porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90;  
"""
num_pessoas = 10

soma_idade = 0

count1_pessoas = 0
count2_pessoas = 0
count3_pessoas = 0

for i in range(num_pessoas):
    print(f"Pessoa {i+1}: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (em quilos): "))
    altura = float(input("Altura (em metros): "))

    soma_idade += idade

    if(peso > 90 and altura < 1.5):
        count1_pessoas += 1

    if(idade >= 10 and idade <= 30):
        count2_pessoas += 1
    
    if(altura > 1.90):
        count3_pessoas += 1

media_idades = soma_idade / num_pessoas

porcent = (count2_pessoas / count3_pessoas) * 100 if count3_pessoas > 0 else 0

print(f"A média das idades das dez pessoas: {media_idades}")
print(f"A quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50: {count1_pessoas}")
print(f"A porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90: {count3_pessoas}%")

