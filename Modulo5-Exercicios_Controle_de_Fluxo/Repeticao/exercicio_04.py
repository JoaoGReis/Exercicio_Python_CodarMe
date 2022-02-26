"""
"Jogo acerte o numero"
o usuario pussui 3 tentativas para tentar acertar o numero.
"""

resposta = 8
i = 1

while i <= 3:
    numero = int(input("Digite um numero: "))

    if numero == resposta:
        print("Parabéns você ganhou!!!!!!")
        break
    elif numero > resposta:
        print("O numero digitado é maior que a resposta!")
    else:
        print("O numero digitado é menor que a resposta!")
    i = i+1

if i > 3:
    print("Você perdeu!")
