"""
O programa recebe um numero inteiro e realiza a soma de todos os numero do 1 até o numero digitado.
"""

numero = int(input("Digite um numero:"))

i = 1
soma = 0

while i <= numero:
    print(i)

    soma = soma+i

    i = i+1

print("O total é:", soma)
