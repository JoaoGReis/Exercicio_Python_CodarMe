"""
Calculadora que recebe 3 valores do usuario sendo 2 numeros com variavel do tipo float 
e um sinal de operação do tipo String
"""

valor_a = float(input("Digite o primeiro numero da operação: "))
valor_b = float(input("Digite o segundo numero da operação: "))


print("---------Operações----------")

print("(+)- Soma")
print("(-)- Subtração")
print("(*)- Multiplicação")
print("(/)- Divisão")
print("(**)- Exponenciação")

operador = input("Digite a operação que deseja realizar:")
print("------------------------------")

if operador == "+":
    print("O resultado é: ", valor_a+valor_b)

elif operador == "-":
    print("O resultado é: ", valor_a-valor_b)

elif operador == "*":
    print("O resultado é: ", valor_a*valor_b)

elif operador == "/" and valor_b == 0:
    print("Não é possivel realizar divisão por zero!")

elif operador == "/":
    print("O resultado é: ", valor_a/valor_b)

elif operador == "**":
    print("O resultado é: ", valor_a**valor_b)
