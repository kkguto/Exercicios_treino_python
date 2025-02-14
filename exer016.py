"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:  

a. Se o usuário informar o valor de A igual a zero. a equação não e do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao usuário;
d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;    
"""

import math

a = int(input("Valor a: "));

if (a == 0):
    print("Encerrado");
    exit();

b = int(input("Valor b: "));
c = int(input("Valor c: "));

delta = b**2 - 4*a*c;

if(delta == 0):
    raiz = -b / (2*a);
    print(f"Raiz: {raiz:.2f}");

elif(delta < 0):
    print("Equação não possui Raizes. \nEncerrando...\n");
    exit();

else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a);
    raiz2 = (-b - math.sqrt(delta)) / (2*a);
    print(f"Raiz 1: {raiz1:.2f}\nRaiz 2: {raiz2:.2f}");

