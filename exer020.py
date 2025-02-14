"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 

As perguntas são:

“Telefonou para a vítima? “
“Esteve no local do crime?”
“Mora perto da vítima? “
“Devia para a vítima? “
“Já trabalhou com a vítima? “

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada 
como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. 

Caso contrário, ele será classificado como “Inocente“.  
"""

resp_sim = 0

respo = input("Telefonou para a vítima? ")
if(respo == 's' or respo == 'S'): 
    resp_sim += 1

respo = input("Esteve no local do crime? ")
if(respo == 's' or respo == 'S'): 
    resp_sim += 1

respo = input("Mora perto da vítima? ")
if(respo == 's' or respo == 'S'): 
    resp_sim += 1

respo = input("Devia para a vítima? ")
if(respo == 's' or respo == 'S'): 
    resp_sim += 1

respo = input("Já trabalhou com a vítima? ")
if(respo == 's' or respo == 'S'): 
    resp_sim += 1

if(resp_sim < 2):
    print("Inocente")
elif(resp_sim == 2):
    print("Suspeita")
elif (resp_sim >=3 and resp_sim <= 4):
    print("Cumplice")
else:
    print("Assassino")
