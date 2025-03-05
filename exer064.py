"""
Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números: adição, subtração, multiplicação e divisão.

O programa deve usar laços de repetição para possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. 

O programa só termina quando for escolhida a opção de saída.  
"""

def Menu():
    print("\nMenu de Opções")
    print("="*35)
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    print("="*35)

def coleta_dados():
    try:
        x = float(input("Primeiro valor: "))
        y = float(input("Segundo valor: "))

        return x, y

    except ValueError:
        print("Valores Invalidos. Tente novamente!")
    

def soma(x, y):
    print(f"{x} + {y} = {x + y}") 

def subtr(x, y):
    print(f"{x} - {y} = {x - y}") 

def mult(x, y):
    print(f"{x} x {y} = {x * y}") 

def div(x, y):
    print(f"{x} / {y} = {x / y :.2f}") 

while True:
    try:
        Menu()
        escolha = int(input("Sua escolha é: "))

        if escolha not in range(0, 5):
            print("\nOpção Invalida\n")
        else:
            x, y = coleta_dados()
            if escolha == 0:
                print("Encerrado")
                break
            elif escolha == 1:
                soma(x, y)

            elif escolha == 2:
                subtr(x, y)

            elif escolha == 3:
                mult(x, y)

            else:
                if y > 0:
                    div(x,y)
                else:
                    print("[ERRO] Divisão com Zero!")
                    
    except ValueError:
        print("[ERRO] Entrada inválida. Digite um número inteiro.")