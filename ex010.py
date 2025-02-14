"""
Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. 
Imprima a mensagem “Bom dia!” ou  “Boa Noite” ou “Valor inválido”, conforme o caso.
"""

periodo = input("Digite seu periodo de estudo (M-matutino ou V-vespertino ou N-noturno): ")

periodo = periodo.upper()

if periodo =='M':
    print("Bom dia!")
elif periodo =='V':
    print("Boa Tarde!")
elif periodo =='N':
    print("Boa Noite!")
else:
    print("Valor Inválido")