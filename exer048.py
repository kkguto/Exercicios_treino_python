"""
Faça um programa que usando laços de repetição receba a idade e o peso de 15 pessoas. 
Calcule e mostre as médias dos pesos das pessoas da mesma faixa etária. 

As faixas etárias são: 

de 1 a 10 anos, 
de ll a 20 anos, 
de 21 a 30 anos 
e maiores de 31 anos.  
"""

count1 =  0
count2 =  0
count3 =  0
count4 =  0

soma_peso1 = 0
soma_peso2 = 0
soma_peso3 = 0
soma_peso4 = 0


for i in range(15):
    print(f"Pessoa {i+1}")
    idade = int(input("Idade: "))
    peso = int(input("Peso (em kg): "))

    if idade > 1 and idade <= 10:
        count1 += 1
        soma_peso1 += peso

    elif 11 >= idade <= 20:
        count2 += 1
        soma_peso2 += peso

    elif 21 >= idade <= 30:
        count3 += 1
        soma_peso3 += peso

    else:
        count4 += 1
        soma_peso4 += peso

media1 = soma_peso1 / count1 if count1 > 0 else 0.0
media2 = soma_peso2 / count2 if count2 > 0 else 0.0
media3 = soma_peso3 / count3 if count3 > 0 else 0.0
media4 = soma_peso4 / count4 if count4 > 0 else 0.0

print(f"Media de 1 a 10 anos: {media1} Kg")
print(f"Media de ll a 20 anos: {media2} Kg")
print(f"Media de 21 a 30 anos: {media3} Kg")
print(f"Media de maiores de 31 anos: {media4} Kg")
