"""
Esse programa cria uma função que retorna o maior numero de uma lista e o idice desse 
numero em uma tupla.
"""

def maior_numero(lista_numeros):
    pos = 0
    num = 0

    for posi in range(0, len(lista_numeros)):

        if lista_numeros[posi] > num:
            num = lista_numeros[posi]
            pos = posi
    return(pos, num)


listas = [1, 8, 3, 4, 5]

print(maior_numero(listas))
