"""
Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.
"""

for i in range(1, 11):
    print(f"\nTabuada do Numero {i}: \n")
    for j in range(1, 11):
        print(f"{j} x {i} = {j * i}")