"""
Faça um programa que verifique (usando if e else) se uma letra digitada é vogal ou consoante.  
"""

vogais = ["a", "e", "i", "o", "u"]

letra = input("Digite um letra: ")

if letra in vogais:
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante")