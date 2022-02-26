"""
Programa de autenticação de usuario, 
verifica se o nome de usuario digitado e a senha estão corretos>
"""

usuario = "admin"
senha = "123123"

nome_usuario = input("Digite o nome de usuario:\n")

senha_usuario = input("Digite a senha:\n")

if nome_usuario == usuario and senha_usuario == senha:
    print("Autenticação fo bem-sucedida.")

elif nome_usuario != usuario and senha_usuario != senha:
    print("Usuario e senha incorretos!")

elif nome_usuario != usuario:
    print("usuario incorreto!")

elif senha_usuario != senha:
    print("senha incorreta!")
