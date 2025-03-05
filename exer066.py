"""
Uma agência bancária possui vários clientes que podem fazer investimentos com rendimentos mensais, conforme a tabela a seguir:

Tipo	Descrição	Rendimento mensal
1	    Poupança	       1,5%
2	   Poupança plus	    2%
3	   Fundos de renda	    4%

Faça um programa que leia o código do cliente, o tipo da conta e o valor investido e que calcule e mostre o rendimento mensal de acordo com o tipo do investimento. 
Ao final do programa mostre o total de juros pagos. 

A leitura terminará quando o código do cliente digitado for menor ou igual a 0.
"""

total_juros = 0

while True:
    try:
        codigo = int(input("Codigo do Cliente: "))

        if codigo <= 0:
            break
        valor_investido = float(input("Valor Investido: "))
        tipo_conta = int(input("Tipo da Conta (1, 2, 3): "))
        
        if tipo_conta == 1:
            rendimento = valor_investido * 0.015
        elif tipo_conta == 2:
            rendimento = valor_investido * 0.02
        elif tipo_conta == 3:
            rendimento = valor_investido * 0.04
        else:
            print("\nTipo Invalido. Tente Novamente!\n")
            continue
        total_juros += rendimento
        print(f"Cliente {codigo}: Rendimento Mensal = R$ {rendimento:.2f}\n")    
    except ValueError:
        print("[ERRO] Entrada inválida. Digite um número inteiro.")
    
print(f"\nTotal de juros pagos: R$ {total_juros:.2f}")