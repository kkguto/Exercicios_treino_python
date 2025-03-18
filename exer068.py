"""
Escreva um procedimento que recebe as 3 notas de um aluno por parâmetro e uma letra. 

Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. 

A média calculada também deve retornar por parâmetro.
"""

def medias(n1, n2, n3, letra):
    if letra == 'A':
        return (n1 + n2 + n3) / 3
    elif letra == 'P':
        return ((n1 * 5) + (n2 * 3) + (n3 * 2)) / (5 + 3 + 2)
    else:
        return 3 / ((1/n1) + (1/n2) + (1/n3))
    
try:
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    n3 = float(input("Terceira nota: "))

    tipo = input("Media (A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica)").upper()
    
    if tipo not in ('A','P', 'H'):
        print("Tipo de media Invalida!")
    else:
        media = medias(n1, n2, n3, tipo)
        print(f"Media das notas: {media:.2f}")
except ValueError:
    print("Erro")