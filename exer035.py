"""
Escreva um programa que lê o tamanho do lado de um quadrado e imprime um quadrado daquele tamanho com asteriscos e espaços em branco. 
Seu programa deve funcionar para quadrados com lados de todos os tamanhos entre 1 e 20.

Para lado igual a 5:
*****
*    *
*    *
*    *
*****
"""

lado = int(input("Digite um numero: "))

for i in range(lado):
    for j in range(lado):
        if(j == 0 or j == lado - 1 or i == 0 or i == lado - 1 ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

