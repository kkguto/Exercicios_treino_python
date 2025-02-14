"""
As organizações CSM resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa 
que calculará os reajustes.  

a. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual;
b. Salários até R$ 280,00 (incluindo): aumento de 20%;
c. Salários entre R$ 280,00 e R$700,00: aumento de 15%;
d. Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
e. Salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado; informe na tela;

a. O salário antes do reajuste;
b. O percentual de aumento aplicado;
c. O valor do aumento;
d. O novo salário, após o aumento.  
"""

salario = float(input("Salario: "))

percen = 0.0

if salario < 280:
    percen = 0.2
    aumento = salario * percen
elif salario >= 280 and salario < 700:
    percen = 0.15
    aumento = salario * percen
elif salario >= 700 and salario < 1500:
    percen = 0.1
    aumento = salario * percen
else:
    percen = 0.05
    aumento = salario * percen

salario_ajustado = salario + aumento
print(f"Salario Anterior: R${salario}\nPercentual de Aumento aplicado: {percen*100}%\nValor de Aumento: R${aumento}\nNovo Salario: R${salario_ajustado}")