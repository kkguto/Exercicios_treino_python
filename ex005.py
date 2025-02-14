"""
Faça um programa para a leitura de duas notas parciais de um aluno.  

A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez;
A mensagem “Reprovado” se a média for menor de do que sete;
"""

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1+n2)/2

if media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção") 
else:
    print("Aprovado")