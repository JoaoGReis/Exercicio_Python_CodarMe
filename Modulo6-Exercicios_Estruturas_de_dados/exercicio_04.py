"""
Esse programa calcula a media da nota de todos os alunos na lista e tupla.
"""


# alunos e suas respectivas notas
alunos = [
    ("alice", 10),
    ("bob", 10),
    ("carlos", 5)

]

soma = 0
for nome, notas in alunos:

    soma = soma+notas

media = soma/len(alunos)

print("A media de notas de todos os lunos é:", media)
