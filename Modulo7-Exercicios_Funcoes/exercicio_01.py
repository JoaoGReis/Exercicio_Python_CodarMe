"""
Esse progra cria uma fução que verifica se um numero é primo ou não.
"""


def n_primo(numero):
    i = 1
    divisor = 0
    while i <= numero:

        if numero % i == 0:
            divisor += 1
        i += 1

    if divisor != 2:
        return False
    else:
        return True


print(n_primo(10))
