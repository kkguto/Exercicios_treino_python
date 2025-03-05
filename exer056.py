"""
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. 
Faça um programa que calcule e mostre:  

A média dos salários do grupo;
A maior e a menor idade do grupo;
A quantidade de mulheres com salário até R$ 200,00;
A idade e o sexo da pessoa que possui o menor salário.   

Finalize a entrada de dados ao ser digitada uma idade negativa.  
"""

maior_idade = 0
menor_idade = int('inf')
menor_salario = float('inf')

soma_salario = 0
count_mulheres = 0
count_total = 0

while True:
    sexo = (input("sexo (M/F): ")).upper()

    if sexo not in ('M', 'F'):
        print("\nSexo Invalido, Tente Novamente!")
        continue

    try:
        idade = int(input("Idade: "))

    except ValueError:
        print("\nIdade invalida. Tente Novamente")
        continue

    try:
        salario = float(input("Salário: "))
    except ValueError:
        print("\nSalário inválido! Digite um número válido.")
        continue
    
    if(salario < 0):
        break

    if salario < menor_salario:
        menor_salario = salario
        idade_menor_salario = idade
        sexo_menor_salario = sexo


    if sexo == 'M' and salario <= 200:
        count_mulheres += 1
    
    if idade > maior_idade:
        maior_idade = idade
    
    if idade < menor_idade:
        menor_idade = idade

    soma_salario += salario
    
    count_total += 1

media_salario = soma_salario / count_total if count_total > 0 else 0.0

print("\nResultados da pesquisa:")
print(f"A média dos salários do grupo: R${media_salario}")
print(f"Maior Idade: {maior_idade} \t Menor Idade: {menor_idade}")
print(f"A quantidade de mulheres com salário até R$ 200,00: {count_mulheres}")

if idade_menor_salario is not None and sexo_menor_salario is not None:
    print(f"A idade e o sexo da pessoa que possui o menor salário: {'Homem' if sexo_menor_salario == 'M' else 'Mulher'}, {idade_menor_salario} anos")
else:
    print("Nenhuma pessoa foi cadastrada.")


