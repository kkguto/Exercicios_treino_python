"""
Faça um programa que receba a idade e o sexo de sete pessoas e que calcule e mostre:

A idade média do grupo;
A idade média das mulheres;
A idade média dos homens;  
"""

soma_idades = 0
soma_idades_mulher = 0
soma_idades_homem = 0

count_homens = 0
count_mulheres = 0

for i in range(7):
    print(f"Pessoa {i+1}: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M - masculino, F - Feminino): ").strip().upper()

    while sexo not in ('M', 'F'):
        print("Opção Invalida. Digite Novamente")
        sexo = input("Sexo (M - masculino, F - Feminino): ").strip().upper()


    if(sexo == 'M'):
        soma_idades_homem += idade
        count_homens += 1
    else:
        soma_idades_mulher += idade
        count_mulheres += 1
    
    soma_idades += idade


media_total = soma_idades // 7
media_homens = soma_idades_homem // count_homens
media_mulhers = soma_idades_mulher // count_mulheres

print(f"A idade média do grupo: {media_total}")
print(f"A idade média das mulheres: {media_mulhers}")
print(f"A idade média dos homens: {media_homens}")
