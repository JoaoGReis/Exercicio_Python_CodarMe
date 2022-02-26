"""
programa recebe um numero digitado pelo usuario e verifica se é um numero primo.
"""

numero = int(input("Digite um numero: "))

i = 1
divisor = 0
while i <= numero:

    if numero % i == 0:
        divisor = divisor + 1

    i = i+1
#-------------------------------------------------#

if divisor != 2:
    print("O numero digitado não é um numero primo!")
else:
    print("O numero digitado é um numero primo!")
