"""
Programa recebe um numero inteiro e imprime todos os numeros pares entre 1 e o numero digitado.
"""

numero = int(input("Digite um numero:"))


i = 1
while i <= numero:

    if i % 2 == 0:
        print(i)

    i = i+1
