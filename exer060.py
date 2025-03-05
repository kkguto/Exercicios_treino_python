"""
Faça um programa que apresente o menu de opções a seguir:  

Menu de opções:  

1. Média aritmética
2. Média ponderada
3. Sair  
Digite a opção desejada:

Na opção 1: receber duas notas, calcular e mostrar a média aritmética.
Na opção 2: receber três notas e seus respectivos pesos, calcular e mostrar a média ponderada.
Na opção 3: sair do programa.  
Verifique a possibilidade de opção inválida, mostrando uma mensagem.  
"""

def Menu():
    print("\nMenu de Opções")
    print("="*30)
    print("1. Média aritmética")
    print("2. Média ponderada")
    print("3. Sair")
    print("=" * 30)

def medias(choice):
    try:
        if choice == 1:
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            return (nota1 + nota2) / 2
        
        elif choice == 2:
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
            p1 = float(input("Peso 1: "))
            p2 = float(input("Peso 2: "))    
            p3 = float(input("Peso 3: "))

            return ((nota1 * p1) + (nota2 * p2) + (nota3 * p3)) / (p1 + p2 + p3)

        else:
            return -1

    except ValueError:
        print("Valor Invalido, Tente novamente!")


while True:
    try:
        Menu()
        choice = int(input("Sua Escolha eh: "))
        if choice in range(1, 4):
            result = medias(choice)
        else:
            print("Opção Invalida. Tente Novamente")

        if result == -1:
            print("\nEncerrado")
            break
        else:
            print(f"Media: {result:.2f}")

    except ValueError:
        print("\nValor Invalido")