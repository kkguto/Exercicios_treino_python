"""
Faça um programa que receba vários números e que calcule e mostre:  

A quantidade de números inferiores a 35;
A média dos números positivos;
A percentagem de números entre 50 e 100 entre todos os números digitados;
A percentagem de números entre 10 e 20 entre os números menores que 50.  
"""

count_inf_35 = 0
count_positivos = 0
count_inf_50 = 0
count_entre_50_100 = 0
count_entre_10_20 = 0

total = 0

while True:
    print(f"\n{total+1}. Numero:")
    print(f"="*30)
    try:
        num = int(input("\nDigite um número (ou -1 para sair): "))
        if num == -1:
            break 
        total += 1

        if num < 35:
            count_inf_35 += 1

        if num > 0:
            count_positivos += 1
            soma_positivos += num

        if 50 <= num <= 100:
            count_entre_50_100 += 1

        if num < 50:
            count_inf_50 += 1
            if 10 <= num <= 20:
                count_entre_10_20 += 1

    except ValueError:
        print("Por favor, digite um número válido.")

media_num_posit = count_positivos / total if total > 0 else 0.0
porcent_entre_50_100 = (count_entre_50_100/total) * 100 if total > 0 else 0
porcent_entre_10_20 = (count_entre_10_20 / total) * 100 if total > 0 else 0

print("\nResultados:")
print(f"Quantidade de números menores que 35: {count_inf_35}")
print(f"Média dos números positivos: {media_num_posit:.2f}")
print(f"Percentual de números entre 50 e 100: {porcent_entre_50_100:.2f}%")
print(f"Percentual de números entre 10 e 20 (entre os menores que 50): {porcent_entre_10_20:.2f}%")