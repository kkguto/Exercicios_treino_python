"""
Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno. 

Dicas:

Três lados formam um triângulo quando a soma de quaisquer dos dois lados é maior que o terceiro.
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input("Lado 1: "));
lado2 = float(input("Lado 2: "));
lado3 = float(input("Lado 3: "));

if((lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2)):
    if(lado1 == lado2 == lado3):
        print("Triângulo Equilátero");

    elif((lado1 == lado2 != lado3) or (lado3 == lado2 != lado1) or (lado1 == lado3 != lado2)):
        print("Triângulo Isósceles");

    else:
        print("Triângulo Escaleno");     
else:
    print("Não pode ser um triângulo");