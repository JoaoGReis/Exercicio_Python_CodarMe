"""
Esse programa recebe tanto uma tupla quanto um dicionario e informa se é menor ou maior de idade.
"""


def maior_idade(p):
    if type(p) == dict:

        if p["idade"] >= 18:
            print(p["nome"], "é maior de idade!")
        else:
            print(p["nome"], "é menor de idade!")
    else:
        if p[1] >= 18:
            print(p[0], "é maior de idade!")
        else:
            print(p[1], " é menor de idade!")


pessoa = {"nome": "Gabriel",
          "idade": 15}

maior_idade(pessoa)

humano = ("josé", 18)
maior_idade(humano)
