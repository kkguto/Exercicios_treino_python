"""
Faça um programa que receba como entrada uma lista de números positivos ou negativos, terminada com o número zero. 

O programa deve usar laços de repetição para produzir como saída a soma dos números positivos, a soma dos números negativos e a soma das duas somas parciais.  
"""

soma_positivos = soma_negativos = 0

while True:
    try:
        num = int(input("Digite um numero (0 encerra): "))
        
        
        if num == 0:
            print("\nEncerrado\n")
            break
        elif num > 0:
            soma_positivos += num
        else:
            soma_negativos += num

    except ValueError:
        print("Valor Invalido")

soma_parcial = soma_positivos + soma_negativos

print(f"Resultado")
print(f"="*35)
print(f"Soma dos Numeros Positivos: {soma_positivos}")
print(f"Soma dos Numeros Negativos: {soma_negativos}")
print(f"Soma Parcial: {soma_parcial}")
print(f"="*35)
