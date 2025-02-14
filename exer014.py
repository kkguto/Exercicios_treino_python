"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 
3% para o Sindicato e que o FGTS corresponde a 11% do salário bruto, mas não é descontado (é a empresa que deposita.)

O salário líquido corresponde ao salário bruto menos os descontos O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
a. Salário Bruto ate R$900,00 (inclusive) – Isento;
b. Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
c. Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
d. Salário bruto acima de 2500 – Desconto de 20%.

Imprima na tela as informações, dispostas conforme o exemplo abaixo, no exemplo valor da hora é 5 e a quantidade de horas é 220.  

Salário bruto (5 * 220)           : R$   1100,00

( – ) IR (5%)                     : R$     55,00

( – ) INSS ( 10% )                 : R$     110,00

FGTS ( 11%)                       : R$     121,00

Total de descontos                 : R$     165,00

Salário Líquido                   : R$     935,00    
"""

valor_hora = float(input("Valor da sua Hora: "));
quant_horas = int(input("Horas Trabalhadas no Mês: "));

salario_bruto = quant_horas * valor_hora;

desc_IR = 0.0;

if(salario_bruto > 0 and salario_bruto <= 900):
    desc_IR += (salario_bruto * 0.0); 

elif(salario_bruto > 900 and salario_bruto <= 1500):
    desc_IR += (salario_bruto * 0.05);
    
elif(salario_bruto > 1500 and salario_bruto <= 2500):
    desc_IR += (salario_bruto * 0.1);

else:
    desc_IR += (salario_bruto * 0.2);

desc_INSS = (salario_bruto * 0.1);
desc_FGTS = (salario_bruto * 0.11);

total_desc = desc_IR + desc_INSS;

salario_liq = salario_bruto - total_desc;
print();

print(f"Salário bruto ({quant_horas} * {valor_hora}) : R$ {salario_bruto}");
print(f"( – ) IR (5%) : R$ {desc_IR}");
print(f"( – ) INSS ( 10% ) : R$ {desc_INSS}");
print(f"FGTS ( 11%) : R$ {desc_FGTS}");
print(f"Total de descontos : R$ {total_desc}");
print(f"Salário Líquido : R$ {salario_liq}");



