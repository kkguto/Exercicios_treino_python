"""
Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
a) A quantidade de pessoas em cada faixa etária;
b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas: 

Até 15 anos
De 16 a 30 anos
De 31 a 45 anos
De 46 a 60 anos
Acima de 61 anos
"""

ate_15 = 0
de_16_a_30 = 0
de_31_a_45 = 0
de_46_a_60 = 0
de_61 = 0

for i in range(15):
    print(f"\nPessoa {i+1}:")
    idade = int(input("Digite a Idade: :"))

    if(idade <= 15):
        ate_15 += 1

    elif(idade >= 16 and idade <= 30):
        de_16_a_30 += 1

    elif(idade >= 31 and idade <= 45):
        de_31_a_45 += 1
    
    elif(idade >= 46 and idade <= 60):
        de_46_a_60 += 1
    else:
        de_61 += 1


porcent_prime = (ate_15 / 15) * 100
porcent_ult = (de_61 / 15) * 100

print("")
print(f"Até 15 anos: {ate_15}")
print(f"De 16 a 30 anos: {de_16_a_30}")
print(f"De 31 a 45 anos: {de_31_a_45}")
print(f"De 46 a 60 anos: {de_46_a_60}")
print(f"Acima de 61 anos: {de_61}")

print(f"Porcentagem da Primeira Faixa: {porcent_prime}%")
print(f"Porcentagem da Segunda Faixa: {porcent_ult}%")


