"""
Faça um programa para calcular n! (Fatorial de n), sendo que o valor inteiro de n é fornecido pelo usuário. Sabe-se que: N! = 1 * 2 * 3 * … (n – 1) * n 0! = 1, por definição; 
"""

fatorial = 1

valor = int(input("Valor: "))

for i in range(1, valor + 1):
    fatorial *= i
    
print(fatorial)