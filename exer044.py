"""
Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:

O preço final para compra à vista tem um desconto de 20%;
A quantidades de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.
Os percentuais de acréscimo seguem a tabela a seguir.  
Quantidade de parcelas	Percentual de acréscimo sobre o preço final

6	3%
12	6%
18	9%
24	12%
30	15%
36	18%
42	21%
48	24%
54	27%
60	30%
"""

preco_carro = float(input("Valor do carro: "))

a_vista = preco_carro - preco_carro*0.2
print(f"Valor à vista: R$ {a_vista}")
print("="*45)
print("N. Parcelas \t Acréscimo(%) \t V. final")
print("="*45)

for i in range(1, 11):
    print(f"{i*6} \t\t {i*3}  % \t\t R$ {preco_carro + preco_carro*((i*3)/100)}")