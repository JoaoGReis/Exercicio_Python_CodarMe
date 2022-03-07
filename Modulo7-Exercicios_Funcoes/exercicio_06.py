"""
Esse programa cria uma função que calcula o fatorial de um numero.
"""


def fatorial(n):
    resultado = 1

    for numeros in range(n, 0, -1):

        resultado = resultado*numeros

    print(" O resultado de ", n, "fatorial é :", resultado)


fatorial(int(input("Digite um numero:")))
