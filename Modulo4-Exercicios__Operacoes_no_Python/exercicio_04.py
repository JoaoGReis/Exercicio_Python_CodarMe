valor_de_compra = float(input("Digite o valor da compra: "))

valor_do_frete = float(input("Digite o valor do frete: "))

programa_de_fidelidade = input(
    "O Cliente é cadastrado no programa de fidelidade? (S)-Sim ou (N)-não.")

cupom = valor_de_compra+valor_do_frete > 100 or programa_de_fidelidade == "s"

print("O cupom é valido?", cupom)
