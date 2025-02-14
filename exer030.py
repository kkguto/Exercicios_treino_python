"""
Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500. 
A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%. 

Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…

Faça um programa que exiba essa tabela de descontos no seguinte formato:  

Valordacompra – porcentagem de desconto – valor final
"""

valor = 500

for i in range(1, 26):
    desconto = valor * (i / 100)
    valor_final = valor - desconto
    
    print(f"R$ {valor} \t {i}% \t R${valor_final:.2}")
    valor += 100