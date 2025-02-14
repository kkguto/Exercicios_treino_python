"""
Faça um programa que verifique (usando if e else) se uma letra digitada é “F” ou “M”. 
Conforme a letra escrever: F – Feminino, M- Masculino, Sexo inválido.  
"""

sexo = input("Digite a letra F - feminino ou M - masculino: ")

if sexo == 'F' or sexo == 'f':
    print("Feminino")
elif sexo == 'M' or sexo == 'm':
    print("Masculino")
else:
    print("Sexo Inválido")