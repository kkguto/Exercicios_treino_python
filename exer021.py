"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:   

Álcool:

Até 20 litros: desconto de 3% por litro
Acima de 20 litros: Desconto de 5% por litro.

Gasolina:

Até 20 litros: desconto de 4% por litro
Acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool. G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente.  
"""

tipo = input("Tipo de Combustivel (A-álcool. G-gasolina): ")
quant_litros = float(input("Quantidade de Litros: "))

valor_ga = 6.40
valor_alc = 3.90


if(tipo.upper() == 'A'):
    preco = valor_alc
    if(quant_litros <= 20):
        desconto = 0.03
    else:
        desconto = 0.05

elif(tipo.upper() == 'G'):
    preco = valor_ga
    if(quant_litros <= 20):
        desconto = 0.04
    else:
        desconto = 0.06

else:
    print("Tipo Invalido")
    exit()

valor_total = preco * quant_litros
valor_final = valor_total - (valor_total * desconto)

print(f"Valor a ser pago: R$ {valor_final:.2f}")