"""
Faça um programa que receba a idade, altura e o peso de 25 pessoas, Calcule e mostre:

A quantidade de pessoas com idade superior a 50 anos;
A média das Alturas das pessoas com idade entre 10 e 20 anos
A porcentagem das pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.  
"""

quant_sup_50 = 0
quant_pessoas_40quilos = 0
quant_pessoas_alt = 0
soma_alt = 0

for i in range(25):
    print(f"\nPessoa {i+1}: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    if idade > 50:
        quant_sup_50 += 1
    
    if idade >= 10 and idade <= 20:
        quant_pessoas_alt += 1
        soma_alt += altura

    if peso <= 40:
        quant_pessoas_40quilos += 1

media =  soma_alt / quant_pessoas_alt if(quant_pessoas_alt > 0) else 0.0
porcentagem = (quant_pessoas_40quilos / 25)*100 if quant_pessoas_40quilos > 0 else 0

print(f"Quantidade de pessoas com idade superior a 50 anos: {quant_sup_50}")
print(f"Média das Alturas das pessoas com idade entre 10 e 20 anos: {media:.2f}")
print(f"Porcentagem das pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas: {porcentagem:.2f}")