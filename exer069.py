"""
Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o 
valor seja primo e Falso em caso contrário.
"""

def eh_primo(num):

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(eh_primo(13))
