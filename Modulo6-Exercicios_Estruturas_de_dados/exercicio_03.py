"""
esse programa calcula a média dos valores de uma lista e restorna um resultado inteiro.
"""


notas = [10, 5, 10, 7]
soma = 0
for nota in notas:
    soma = soma+nota

media = soma//len(notas)
print(media)
