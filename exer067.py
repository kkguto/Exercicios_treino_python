"""
Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3.P .R3).
"""
import math

def volume_esfera(raio):
    pi = math.pi
    return (4/3) * pi * raio**3


print(f"Volume = {volume_esfera(5):.2f}")