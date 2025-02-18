"""
Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A - Azul, P- Preto, V- Verde e C- Castanho)
e a cor dos cabelos (P - Preto, C- Castanho, L - Louro e R-Ruivo) de 20 pessoas e que calcule e mostre: 
 
A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos;
A média das idades das pessoas com altura inferior a 1,50;
A porcentagem de pessoas com olhos azuis entre as pessoas analisadas;
A quantidade de pessoas ruivas que não possuem olhos azuis;  
"""

quant_idade50_quilos60 = 0
quant_altura = 0
soma_idade = 0
quant_ruivas_n_olhos_azul = 0
quant_olhos_azuis = 0

for i in range(20):
    print(f"Pessoa {i+1}:")

    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    peso = float(input("Peso (em quilos): "))
    olho = input("Cor dos olhos (A - Azul, P- Preto, V- Verde e C- Castanho): ").strip().upper()

    while olho not in ('A', 'P', 'V', 'C'):
        print("\nOpção Invalida. Digite novamente") 
        olho = input("Cor dos olhos (A - Azul, P- Preto, V- Verde e C- Castanho): ").strip().upper()

    cabelo = input("Cor do cabelo (P - Preto, C- Castanho, L - Louro e R-Ruivo): ").strip().upper()

    while cabelo not in ('L', 'P', 'R', 'C'):
        print("\nOpção Invalida. Digite novamente") 
        cabelo = input("Cor do cabelo (P - Preto, C- Castanho, L - Louro e R-Ruivo): ").strip().upper()

    if idade > 50 and peso < 60:
        quant_idade50_quilos60 += 1
    
    if altura < 1.5:
        soma_idade += idade
        quant_altura += 1

    if olho == 'A':
        quant_olhos_azuis += 1

    if cabelo == 'R' and olho != 'A':
        quant_ruivas_n_olhos_azul += 1


media_idades = soma_idade / quant_altura
porcentagem = (quant_olhos_azuis / 20) * 100

print(f"A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos: {quant_idade50_quilos60}")
print(f"A média das idades das pessoas com altura inferior a 1,50: {media_idades}")
print(f"A porcentagem de pessoas com olhos azuis entre as pessoas analisadas: {porcentagem}")
print(f"A quantidade de pessoas ruivas que não possuem olhos azuis: {quant_ruivas_n_olhos_azul}")





