"""
Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1. 
Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre:

A média das idades das pessoas que responderam ótimo;
A quantidade de pessoas que respondeu regular;
A percentagem de pessoas que respondeu bom entre todos os espectadores analisados.  
"""

count_otimo = 0
count_bom = 0
count_regular = 0

soma_idade_otimo = 0

for i in range(5):
    print()
    print("="*35)
    print(f"Espectador {i+1}:")
    print("="*35)
    idade = int(input("Idade: "))
    opiniao = int(input("Opiniao (ótimo - 3, bom - 2, regular - 1): "))

    while opiniao != 3 and opiniao != 2 and opiniao != 1:
        print("Opiniao Invalida. Tente Novamente!")
        opiniao = int(input("Opiniao (ótimo - 3, bom - 2, regular - 1): "))

    if(opiniao == 1):
        count_regular += 1


    elif(opiniao == 2):
        count_bom += 1

    else:
        count_otimo += 1
        soma_idade_otimo += idade        

media_idade_otimo = soma_idade_otimo // idade if (idade > 0) else 0
porcen = (count_bom / 15) * 100

print(f"A média das idades das pessoas que responderam ótimo: {media_idade_otimo}")
print(f"A quantidade de pessoas que respondeu regular: {count_regular}")
print(f"A percentagem de pessoas que respondeu bom entre todos os espectadores analisados: {porcen} %")
