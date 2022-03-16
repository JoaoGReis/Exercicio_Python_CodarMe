from usuario import Usuario
from administrador import Administrador

u = Usuario("Gabriel", "gabriel@gabriel.com")
a = Administrador("Admin", "admin@exemplo.com")

u.imprime_usuario()
a.imprime_usuario()


print(Usuario.quatidade)
