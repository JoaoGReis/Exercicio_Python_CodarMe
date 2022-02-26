"""
Esse programa lê numeros inteiros positivos digitados pelo usarios e armazena em uma lista, 
o programa para somente quando é digitado um numero negativo.
"""


i = 0
numeros = []

while i >= 0:
    i = int(input("Digite um numero numero inteiro:"))

    if i >= 0:
        numeros.append(i)


print(numeros)
