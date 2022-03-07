"""
Esse programa cria uma função que verifica se um elemento esta em uma lista .
"""


def comparacao(lista, elemento):
    result = False

    for i in lista:
        if i == elemento:
            result = True

    print(result)


valores = [6, 3, 8, 10]

e = 8

comparacao(valores, e)
