"""
Faça um programa que receba a idade e a altura de várias pessoas e que calcule e mostre a média das alturas das pessoas com mais de 50 anos. 
Para encerrar a entrada de dados digite idade menor ou igual a zero.    
"""

soma_altura = 0
count_total = 0

while True:
    try:
        idade = int(input("Idade: "))

        if idade <= 0:
            break

        altura = float(input("Altura: "))

        if altura <= 0:
            print("Altura inválida! Deve ser maior que zero.")
            continue  # Volta para pedir os valores novamente
        
        if idade > 50:
            soma_altura += altura

        count_total += 1

    except ValueError:
        print("Valores Invalidos")
    
media = soma_altura/count_total if count_total > 0 else 0

print(f"Media das alturas das pessoas com mais de 50 anos: {media}")