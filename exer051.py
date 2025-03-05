"""
O sistema de avaliação de uma determinada disciplina obedece aos seguintes critérios: 

Durante o semestre são dadas três notas;
A nota final é obtida pela média aritmética das três notas;
É considerado aprovado o aluno que obtiver a nota final superior ou igual a 6 e que tiver comparecido a um mínimo de 40 aulas.  
"""

soma_notas = 0
num_aulas = int(input("Numero de aulas que o Aluno Compareceu: "))

for i in range(3):
    soma_notas += float(input(f"Nota {i+1}: "))

media = soma_notas / 3
estado = "Aprovado" if media >= 6 and num_aulas >= 40 else "Reprovado"

print(f"Estado: {estado}\nNum. Aulas: {num_aulas}\nMédia: {media:.2f}")