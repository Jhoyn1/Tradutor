import json
import os

try:
    with open("pessoas.json", "r", encoding="UTF-8") as arquivo:
        pessoas = json.load(arquivo)
except FileNotFoundError:
    pessoas = {}

while True:
    print("1 - Cadastrar pessoa")
    print("2 - Procurar pessoa cadastrada")
    print ("3 - Sair")

    opcao = input("Qual opção você quer? ")

    if opcao == '1':
        nome = input("Insira o nome completo: ")
        idade = int(input("Insira a idade: "))
        email = input("Insira o email: ")
        cpf = int(input("Insira o CPF: "))
        EC = input ("Insira o estado civil: ")
        endereco = input("Insira o endereço: ")

        pessoas[nome] = {
        "idade": idade,
        "email": email,
        "cpf": cpf,
        "EC": EC,
        "endereco": endereco
        }

        with open("pessoas.json", "w", encoding="UTF-8") as arquivo:
            json.dump(pessoas, arquivo, indent=4, ensure_ascii=False)
        
        print ("Pessoa cadastrada com sucesso")
    
    elif opcao == '2':
        nome = input("Insira o nome da pessoa que quer encontrar: ")

        if nome in pessoas:
            print(f"\nNome: {nome}")
            print(f"Idade: {pessoas[nome]['idade']}")
            print(f"Email: {pessoas[nome]['email']}")
            print(f"CPF: {pessoas[nome]['cpf']}")
            print(f"EC: {pessoas[nome]['EC']}")
            print(f"endereco: {pessoas[nome]['endereco']}")
        else:
            print("Pessoa não encontrada")

    elif opcao == '3':
        print("Saindo . . .")
        break
    else:
        print("Opção invalida")



