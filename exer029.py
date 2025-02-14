"""
Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000).  
Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.
"""

faturamento = 0

for i in range(5):
    faturamento += float(input(f"Digite o valor do cliente {i + 1}: "))

if(faturamento > 54000):
    print(f"O faturamento foi superado em R$ {faturamento - 54000 :.2}!")
else:
    print("Infelizmente o faturamento não foi superado")