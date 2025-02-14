"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre o mais barato.  
"""

preco1 = float(input("Preço 1: "))
preco2 = float(input("Preço 2: "))
preco3 = float(input("Preço 3: "))

menor_preco = preco1
produto = 1
if menor_preco > preco2:
    menor_preco = preco2
    produto = 2

if menor_preco > preco3:
    menor_preco = preco3
    produto = 3

print(f"Produto {produto} e custa R${menor_preco}")