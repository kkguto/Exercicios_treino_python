"""
Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba código e valor de 15 transações usando laços de repetição. Calcule e mostre:  

O valor total das compras à vista
O valor total das compras a prazo c.   
O valor total das compras efetuadas
O valor da primeira prestação das compras a prazo, sabendo-se que essas serão pagas em três vezes 
"""
valor_vista = 0
valor_prazo = 0
valor_total = 0

for i in range(15):

    valor = float(input("Valor da compra: "))
    codigo = input("Tipo de Transação (V - à vista ou P - a prazo): ").strip().upper()

    while codigo != 'V' and codigo != 'P':
        print("Codigo Invalido")

        codigo = input("Tipo de Transação (V - à vista ou P - a prazo): ").strip().upper()

    if(codigo == 'V'):
        valor_vista += valor
    else:
        valor_prazo += valor

    valor_total += valor

print(f"Valor a vista: {valor_vista}")
print(f"Valor a prazo: {valor_prazo}")
print(f"Valor a Total das Compras: {valor_total}")
print(f"Valor das primeiras prestações a prazo: {valor_prazo/3 :.2f}")
