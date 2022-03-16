"""
Esse modulo cria a classe usuario
"""


class Usuario:
    quatidade = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.quatidade += 1

    def imprime_usuario(self):
        print(f'"{self.nome} ({self.email})"')
