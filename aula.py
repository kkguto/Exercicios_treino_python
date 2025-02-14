#Função print imprimi/mostra algo no Terminal/Tela

"""

3 aspas abrindo e 3 aspas fechando == docstring 
Docstrig usado para escrever notas

"""

print(123)#number
print('123')#string
print(3 < 0)#boolen FALSE/TRUE
print(123, 456, '6666', 3>5) #eh possivel colocar mais de um argumento dentro da função print()
print(12, 34, sep="...") #sep="" == Separador == Argumento Nomeado


#\r == return e \n == line feed --> Quebra de linha 

#IMC
print()
nome = 'ZZZZ'
peso = 95
altura = 1.8
imc = peso/(altura **2)

print(f'{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é de {imc:.2f}')

# valor1 = (input('Digite uma valor: '))
# valor2 = (input('Digite outro valor: '))

# if valor1 > valor2:
#     print(f'{valor1 = } é maior que {valor2 = }')
# else:
#     print(f'{valor2 = } é maior que {valor1 = }')

# and --> todos os valores tem que ser verdadeiros
# or --> apenas um valor precisa ser verdadeiro 

# entrada = input('[E] Entrar\n[S] Sair:\n').lower()
# senhaDigitada = input('Senha: ')

# senhaReal = '123456'

# if entrada == 'e' and senhaDigitada == senhaReal:
#     print('Entrar')
# elif entrada == 's':
#     print('Sair')
# else:
#     print('Escolha uma opção valida')
    
print(True and True and True) #Retorna True
print(True and True and False) #Retorna False
print(True or False) #Retorna True

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: ^12}')

# name = input('Digite seu nome >>') 
# age = (input('Digite sua idade >>')) 
# if name and age:
#     print(f'Seu nome é {name}')
#     print(f'Seu nome ao contrario é {name[-1: -len(name) -1 :-1]}')
#     print(f'O seu nome tem {len(name)} letras')
#     print(f'A primeira letra do nome é {name[0].upper()}')
#     print(f'A ultima letra do nome é {name[-1].upper()}')
#     if ' ' in name:
#         print('Seu nome contem espaços')
#     else:
#         print('Seu nome nao contem espaços')
# else:
#     print('Voce deixo campos vazios')

# numero = (input('Digite um numero: ')) 
# numero.isdigit() #verifica se é um numero inteiro  
try:  
    print(numero)
    print(int(numero))
    print(float(numero)*2)
except:
    print('Não digitado')
#Try e except captura erros

velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

mutado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
velocidade_nao_permitida = velocidade > RADAR_1

if velocidade_nao_permitida:
    print('Velocidade acima do permitido')

if mutado and velocidade_nao_permitida:
    print('carro mutado')

#-----------------------------------------------------------
#VERIFICADOR DE NUMEROS PARES E IMPARES

# n1 = input('Digite um numero inteiro >> ')
# if n1.isdigit():
#     if int(n1) % 2 == 0:
#         print('PAR')
#     else:
#         print('ÍMPAR')
# else:
#     print('Não é um numero inteiro') 


# try:
#     if int(n1) % 2 == 0:
#         print('PAR')
#     else:
#         print('ÍMPAR')
# except:
#     print('Não é um numero inteiro') 
# -----------------------------------------------------------


#HORASS
#-------------------------------------------------------------
# x = input('Digite a hora em numeros inteiros (0 - 23) >> ')

# if x.isdigit():
#     hora = int(x)
#     if hora >= 0 and hora <= 11:
#         print('BOM DIA')
#     elif hora >= 12 and hora <= 17:
#         print('BOA TARDE')
#     elif hora >= 17 and hora <= 23:
#         print('BOA NOITE')
#     else:
#         print('NÃO CONHEÇO ESSA HORA')    
# else:
#     print('A hora não está com numero inteiro')

# try:
#     hora = int(x)
#     if hora >= 0 and hora <= 11:
#         print('BOM DIA')
#     elif hora >= 12 and hora <= 17:
#         print('BOA TARDE')
#     elif hora >= 17 and hora <= 23:
#         print('BOA NOITE')
#     else:
#         print('NÃO CONHEÇO ESSA HORA')  
# except:
#     print('A hora não está com numero inteiro')
#-------------------------------------------------------------

# name = input('Digite seu nome >> ')
# tama_name = len(name)
# if tama_name > 1:
#     if tama_name <= 4:
#         print('nome muito curto')
#     elif tama_name >=5 and tama_name <=6:
#         print('Seu nome é normal')
#     elif tama_name > 6:
#         print('Nome muito grande')
# else:
#     print('Digite mais de uma letra')


