"""
Esse programa imprime o maior numero da lista.
"""

lista = [1, 3, 8, 5]

maior = 0

for numero in lista:
    if numero > maior:
        maior = numero

print(maior)

