"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:  

1, 2, 3, 4	Votos para os respectivos candidatos
5	Voto nulo
6	Voto em branco
Faça um programa que calcule e mostre:  

O total de votos para cada candidato;
O total de votos nulos:
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.  
Para finalizar o conjunto de votos, tem-se o valor zero.  
"""

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

total_votos = 0

while True:

    try:
        voto = int(input("Voto (1 a 6 e 0 para finalizar): "))

        if voto == 0:
            print("\nEncerrado\n")
            break
        elif voto == 1:
            count1 += 1

        elif voto == 2:
            count2 += 1

        elif voto == 3:
            count3 += 1

        elif voto == 4:
            count4 += 1

        elif voto == 5:
            count5 += 1

        elif voto == 6:
            count6 += 1

        else:
            print("Valor Invalido. Digite Novamente")
            continue

        total_votos += 1

    except ValueError:
        print("Valor Invalido")

porcent_nulos = (count5 / total_votos) * 100 if total_votos > 0 else 0
porcent_brancos = (count6 / total_votos) * 100 if total_votos > 0 else 0

print("\nResultado: ")
print("="*35)
print(f"Candidato 1: {count1}")
print(f"Candidato 2: {count2}")
print(f"Candidato 3: {count3}")
print(f"Candidato 4: {count4}")
print(f"O total de votos nulos: {count5}")
print(f"O total de votos em branco: {count6}")
print(f"A percentagem de votos nulos sobre o total de votos: {porcent_nulos}%")
print(f"A percentagem de votos em branco sobre o total de votos: {porcent_brancos}%")
print("=" * 40)