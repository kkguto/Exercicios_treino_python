"""
Escreva um aplicativo que recebe inteiro e mostra os números pares e ímpares (separados), de 1 até esse inteiro.
"""

num = int(input("Digite um numero: "))

pares = []
impares = []

for i in range(1, num+1):
    if(i % 2 == 0):
        pares.append(i)
    else:
        impares.append(i)

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")