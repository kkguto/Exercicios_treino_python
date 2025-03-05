"""
Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma cidade, em um determinado dia. 
Para cada casa consultada foi fornecido o número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo aquele canal. 
Se a televisão estivesse desligada, nada era anotado, ou seja, essa casa não entrava na pesquisa. Faça um programa que:  

Leia um número indeterminado de dados (número do canal e o número de pessoas que estavam assistindo);
Calcule e mostre a percentagem de audiência de cada canal.
Para encerrar a entrada de dados digite o número do canal ZERO.  
"""

count_canal4 = 0
count_canal5 = 0
count_canal7 = 0
count_canal12 = 0

count_total_pessoas = 0
i = 0

while True:
    print(f"\nCasa {i+1}")
    num_canal = int(input("Numero do Canal (4, 5, 7, 12): "))

    if num_canal == 0:
        break

    if num_canal != 4 and num_canal != 5 and num_canal != 7 and num_canal != 12:
        print("\nNumero de canal invalido. Digite novamente!\n")
        continue

    count_pessoas = int(input("Numero de Pessoas Assistindo: "))

    if num_canal == 4:
        count_canal4 += count_pessoas

    elif num_canal == 5:
        count_canal5 += count_pessoas

    elif num_canal == 7:
        count_canal7 += count_pessoas

    else:
        count_canal12 += count_pessoas

    count_total_pessoas += count_pessoas
    i += 1

porcent_canal4 = (count_canal4/count_total_pessoas)*100 if count_total_pessoas > 0 else 0
porcent_canal5 = (count_canal5/count_total_pessoas)*100 if count_total_pessoas > 0 else 0
porcent_canal7 = (count_canal7/count_total_pessoas)*100 if count_total_pessoas > 0 else 0
porcent_canal12 = (count_canal12/count_total_pessoas)*100 if count_total_pessoas > 0 else 0

print("\nResultados:")
print(f"Porcentagem do canal 4: {porcent_canal4}%")
print(f"Porcentagem do canal 5: {porcent_canal5}%")
print(f"Porcentagem do canal 7: {porcent_canal7}%")
print(f"Porcentagem do canal 12: {porcent_canal12}%")