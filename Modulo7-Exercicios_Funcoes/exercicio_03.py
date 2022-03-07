"""
Esse programa cria uma função que verifica se uma pessoa é maior ou menor de idade.
"""


def maior_idade(p):

    if p[1] >= 18:
        print("Maior de idade!")
    else:
        print("Menor de idade!")


pessoa = ("Gabriel", 15)

maior_idade(pessoa)
