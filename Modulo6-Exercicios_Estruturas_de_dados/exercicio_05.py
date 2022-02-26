"""
Esse programa calcula a media de nos que estão em um dicionario dentro de uma lista.
"""


# Alunos e suas notas representados através de dicionários
alunos = [
    {
        "nome": "alice",
        "nota": 8,
    },
    {
        "nome": "Bob",
        "nota": 7,
    },
    {
        "nome": "Carlos",
        "nota": 9,
    }

]

soma = 0

for notas in alunos:

    soma = soma+notas['nota']


media = soma/len(alunos)
print(media)
