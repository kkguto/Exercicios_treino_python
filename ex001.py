"""
Faça um programa que peça dois números e verifique (usando if e else) e imprima o maior deles  
"""

x = float(input("Digite o primeiro Número: "))
y = float(input("Digite o segundo Número: "))

if x > y:
    print(f"{x} é maior que {y}")
else:
    print(f"{y} é maior {x}")