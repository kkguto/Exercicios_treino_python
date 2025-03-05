"""
Faça um programa que leia um conjunto de dados contendo o número da matrícula, as três notas e a frequência (número de aulas frequentadas) de dez alunos.   

Calcule e mostre:

Para cada aluno o número da matrícula, a nota final e a mensagem (aprovado ou reprovado);
A maior e a menor nota da turma;
O total de alunos reprovados;
A percentagem de alunos reprovados por frequência abaixo da mínima necessária.  
"""

MIN_FREQ = 40
NUM_ALUNOS = 10

total_reprovados = 0
total_reprovados_frequencia = 0

maior = 0
menor = 10

def calculo_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def verificar_aprovacao(media, frequencia):
    if(media >= 6.5 and frequencia >= MIN_FREQ):
        return "Aprovado"
    else:
        total_reprovados += 1
        if(frequencia < MIN_FREQ):
            total_reprovados_frequencia += 1
        return "Reprovado"

for i in range (NUM_ALUNOS):
    num_matricula = int(input("Numero da matricula: "))
    frequencia = int(input("Numero de aulas frequentadas: "))
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))

    media = calculo_media(nota1, nota2, nota3)
    status = verificar_aprovacao(media, frequencia)

    if(maior > media):
        maior = media

    if(menor < media):
        menor = media   

    print(f"Matrícula: {matricula}, Nota Final: {media:.2f}, Status: {status}\n")
    
percentual_reprovados_frequencia = (total_reprovados_frequencia / NUM_ALUNOS) * 100

print(f"Maior nota da turma: {maior_nota:.2f}")
print(f"Menor nota da turma: {menor_nota:.2f}")
print(f"Total de alunos reprovados: {total_reprovados}")
print(f"Percentagem de alunos reprovados por frequência: {percentual_reprovados_frequencia:.2f}%")
    

    
