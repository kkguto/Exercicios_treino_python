"""
Faça um programa que apresente o menu de opções a seguir, que permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. 
Verificar a possibilidade de opção inválida e não se preocupar com as restrições, como salário inválido.  

Menu de opções:  

1. Novo salário
2. Férias
3. Décimo terceiro
4. Sair  
Digite a opção desejada :

Na Opção 1: receber o salário de um funcionário, calcular e mostrar o novo salário usando as regras a seguir.  

Salários	Percentagem de aumento
Até R$ 350,00	15%
De R$ 350,00 a R$ 600,00	10%
Acima de R$ 600,00	5%
Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor de suas férias. Sabe-se que as férias equivalem ao seu salário acrescido de l/Ê.  

Na opção 3: receber o salário de um funcionário e o número de meses de trabalho na empresa, no máximo 12, calcular e mostrar o valor do décimo terceiro. 
Sabe-se que o décimo terceiro equivale ao seu salário multiplicado pelo número de meses de trabalho dividido por 12.  

Na opção 4: sair do programa.  
"""

def Menu():
    print("==Menu de opções==")
    print("=" * 35)
    print("1. Novo salário")
    print("2. Férias")
    print("3. Décimo terceiro")
    print("4. Sair ")
    print("=" * 35)

def Novo_salario(salario):
    if salario <= 350:
        return salario + (salario*0.15)
    elif salario > 350 and salario <= 600:
        return salario + (salario*0.1)
    else:
        return salario + (salario*0.05)

def Ferias(salario):
    return salario + (salario / 3)

def Decimo_terceiro(salario, num_meses):
    return salario * (num_meses / 12)

while True:
    try:
        Menu()
        escolha = int(input("Digite a opção desejada: "))

        if escolha == 4:
            print("Encerrado")
            break
        elif escolha == 1:
            try:
                salario = float(input("Salario do Funcionario: "))
                if salario >= 0:
                    result = Novo_salario(salario)
                else:
                    print("Salario Invalido. Digite um Valor Positivo!")
                    continue
                print(f"Novo Salario: R${result:.2f}")

            except ValueError:
                print("[ERRO] Entrada inválida. Digite um Salario Valido.")

        elif escolha == 2:
            try:
                salario = float(input("Salario do Funcionario: "))
                if salario >= 0:
                    result = Ferias(salario)
                else:
                    print("Salario Invalido. Digite um Valor Positivo!")
                    continue

                print(f"Ferias: R${result:.2f}")

            except ValueError:
                print("[ERRO] Entrada inválida. Digite um Salario Valido.")
     
        elif escolha == 3:
            try:
                salario = float(input("Salario do Funcionario: "))
                num_meses = int(input("Numero de Meses trabalhados: "))

                if salario > 0 and num_meses >= 1 and num_meses <= 12:
                    result = Decimo_terceiro(salario, num_meses)
                else:
                    print("Entrada inválida! Certifique-se de que o salário seja positivo e os meses estejam entre 1 e 12.")
                    continue

                print(f"Decimo Tercero Salario: R${result:.2f}")

            except ValueError:
                print("[ERRO] Entrada inválida. Digite um Salario Valido.")
        else:
            print("\nOpção inválida! Escolha uma opção entre 1 e 4.\n")

    except ValueError:
        print("[ERRO] Entrada inválida. Digite um número inteiro.")
