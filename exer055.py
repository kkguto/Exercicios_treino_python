"""
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos. 
A prefeitura deseja saber:  

A média do salário da população;
A média do número de filhos;
O maior salário;
A percentagem de pessoas com salários até R$ 150,00.   

O final da leitura de dados dar-se-á com a entrada de um salário negativo.  
"""

i = 0

maior_salario = 0
soma_salario = 0
soma_filhos = 0
count_salario150 = 0
count_total = 0

while True:
    print(f"Pessoa {i+1}")
    salario = float(input("Salario: "))

    if salario < 0:
        break

    if salario <= 150:
        count_salario150 += 1

    if salario >= maior_salario:
        maior_salario = salario 

    soma_salario += salario

    num_filhos = int(input("Numeros de Filhos: "))
    soma_filhos += num_filhos

    count_total += 1
    i += 1

media_salario = (soma_salario / count_total) if count_total > 0 else 0.0
media_filhos = (soma_filhos // count_total) if count_total > 0 else 0

porcentagem = (count_salario150 / count_total) * 100 if count_total > 0 else 0

print(f"Media de Salario: {media_salario:.2f}")
print(f"Media de Filhos: {media_filhos}")
print(f"Maior Salario: {maior_salario:.2f}")
print(f"Porcentagem de pessoas com salários até R$ 150,00: {porcentagem:.2f}%")