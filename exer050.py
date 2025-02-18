"""
Uma firma fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um novo produto lançado no mercado. Para isso forneceu o sexo do entrevistado e sua resposta (S - Sim ou N - Não). 
Sabe-se que foram entrevistadas dez pessoas. Faça um programa que calcule e mostre:

O número de pessoas que respondeu sim;
O número de pessoas que respondeu não;
O número de mulheres que respondeu sim;
A percentagem de homens que respondeu não entre todos os homens analisados.   
"""

count_sim = 0
count_nao = 0

count_homens = 0
count_homens_nao = 0
count_mulheres_sim = 0

for i in range(10):
    sexo = input("Sexo (M - Masculino ou F - Feminino): ").strip().upper()
    while sexo not in ('M', 'F'):
        print("Sexo Invalida. Tente Novamente!")
        sexo = input("Sexo (M - Masculino ou F - Feminino): ").strip().upper()

    resp = input("Resposta (S - Sim ou N - Não): ").strip().upper()
    while resp not in ('S', 'N'):
        print("Resposta Invalida. Tente Novamente!")
        resp = input("Resposta (S - Sim ou N - Não): ").strip().upper()

    if(sexo == 'M'):
        count_homens += 1
    
    if(sexo == 'M' and resp == 'N'):
        count_homens_nao += 1
    
    if(sexo == 'F' and resp == 'S'):
        count_mulheres_sim += 1
    
    if(resp == 'S'):
        count_sim += 1
    else:
        count_nao += 1
    
porcent = (count_homens_nao / 10) * 100

print(f"O número de pessoas que respondeu sim: {count_sim}")
print(f"O número de pessoas que respondeu não: {count_nao}")
print(f"O número de mulheres que respondeu sim: {count_mulheres_sim}")
print(f"A percentagem de homens que respondeu não entre todos os homens analisados: {porcent:.2f}%")