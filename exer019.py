"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número e:

Par ou ímpar;
Positivo ou negativo;
"""

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

operacao = input("Digite o sibulo da operação que deseja realizar (+, -, * , /): ")

if(operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/"):
    print("Essa Operaçao eh invalida")
    exit()
else:
    if(operacao == "+"):
        print(f"{num1} + {num2} = {num1 + num2}")
        if(num1+num2 > 0):
            print("Valor Positivo")
        else:
            print("Valor Negativo")
        
        if(num1+num2 % 2 == 0):
            print("Par")
        else:
            print("Impar")
    elif(operacao == "-"):
        print(f"{num1} - {num2} = {num1 - num2}")
        if(num1-num2 > 0):
            print("Valor Positivo")
        else:
            print("Valor Negativo")
        
        if(num1-num2 % 2 == 0):
            print("Par")
        else:
            print("Impar")
    elif(operacao == "*"):
        print(f"{num1} * {num2} = {num1 * num2}")
        if(num1*num2 > 0):
            print("Valor Positivo")
        else:
            print("Valor Negativo")
        
        if(num1*num2 % 2 == 0):
            print("Par")
        else:
            print("Impar")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
        if(num1/num2 > 0):
            print("Valor Positivo")
        else:
            print("Valor Negativo")
        
        if(num1/num2 % 2 == 0):
            print("Par")
        else:
            print("Impar")       