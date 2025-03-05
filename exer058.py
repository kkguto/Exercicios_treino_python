"""
Faça um programa que receba o tipo da ação, ou seja, uma letra a ser comercializada na bolsa de valores, 
o preço de compra e o preço de venda de cada ação e que calcule e mostre:  

O lucro de cada ação comercializada;
A quantidade de ações com lucro superior a R$ 1.000,00;
A quantidade de ações com lucro inferior a R$ 200,00;
O lucro total da empresa   

Finalize com o tipo de ação “F”.  
"""

count_sup = 0
count_inf = 0
soma_lucro = 0
i = 0

while True:

    print(f"Ação {i+1}: ")

    acao = input("\nNumero da Ação (digite 'F' para encerrar): ").upper()
    if acao.isdigit():
        print("Ação Invalida. Tente Novamente!")
        continue

    if acao == 'F':
        break
    
    try:
        preco_compra = float(input("Preço da Compra: "))
        preco_venda = float(input("Preço da Venda: "))
    except ValueError:
        print("Valor inválido. Digite um número válido.")
        continue

    lucro = preco_venda - preco_compra
    soma_lucro += lucro

    print(f"Lucro da ação {acao}: R$ {lucro:.2f}")

    if lucro >= 1000:
        count_sup += 1
    
    if lucro <= 200:
        count_inf += 1

    i += 1


print("==Resultados==")
print("="*30)
print(f"A quantidade de ações com lucro superior a R$ 1.000,00: {count_sup}")
print(f"A quantidade de ações com lucro inferior a R$ 200,00: {count_inf}")
print(f"O lucro total da empresa: {soma_lucro}")
