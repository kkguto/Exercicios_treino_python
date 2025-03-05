"""
Uma empresa deseja aumentar seus preços em 20%. Faça um programa que leia o código e o preço de custo de cada produto e que 
calcule o novo preço. 

Calcule também a média dos preços com e sem aumento. 

Mostre o código e o novo preço de cada produto e, no final, as médias. 

A entrada de dados deve terminar quando for lido um código de produto negativo. 
"""

soma_preco_sem_aumento = 0
soma_preco_com_aumento = 0

count_total = 0

while True:
    print(f"\nProduto {count_total+1}")
    print(f"====================")
    codigo = int(input("Codigo: "))

    if codigo < 0 : 
        break
    
    try:
        preco = float(input("Preço do Produto: "))

    except ValueError:
        print("Preço Invalido. Tente Novamente!")
        continue

    soma_preco_sem_aumento += preco
    soma_preco_com_aumento += preco + (preco * 0.2)

    print(f"Cod. Produto: {codigo} \t Preço Inicial: R${preco} \t Preço com Aumento: R${preco + (preco * 0.2)}")
    count_total += 1

media_sem_aumento = soma_preco_sem_aumento / count_total if count_total > 0 else 0.0
media_com_aumento = soma_preco_com_aumento / count_total if count_total > 0 else 0.0

print("\n========== RESUMO ==========")
print(f"Media com Aumento: R${media_com_aumento}\nMedia sem Aumento: R${media_sem_aumento}")
