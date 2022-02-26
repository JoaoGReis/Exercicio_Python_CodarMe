"""
Programa recebe  um numero inteiro e imprime:

->"Fizz", caso seja multiplo de 3.
->"Buzz", caso seja multiplo de 5.
->"FizzBuzz", caso seja multiplo de 3 e 5.

"""

numero = int(input("Digite um numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")

elif numero % 5 == 0:
    print("Buzz")

elif numero % 3 == 0:
    print("Fizz")
