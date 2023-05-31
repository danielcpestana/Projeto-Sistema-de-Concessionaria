import re
from lib.interface.interface import *


def formatar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    # Formata o CPF com pontos e hífen
    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    return cpf_formatado


def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito_verificador_1 = 0 if resto < 2 else 11 - resto
    if int(cpf[9]) != digito_verificador_1:
        return False
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito_verificador_2 = 0 if resto < 2 else 11 - resto
    if int(cpf[10]) != digito_verificador_2:
        return False

    return True
def cadastrar_cliente():
    cabeçalho(" Cadastrar Cliente ")
    try:
        nome = input("Digite o nome do cliente: ").upper()
        cpf = input("Digite o CPF do cliente: ")

        # Valida o CPF
        cpf_valido = validar_cpf(cpf)

        if not cpf_valido:
            print("CPF inválido. Por favor, digite novamente.")
            return

        # Formata CPF, telefone e endereço
        cpf_formatado = formatar_cpf(cpf)

        with open("clientes.txt", "a") as arquivo:
            arquivo.write(f"{nome},{cpf_formatado}\n")

        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao cadastrar o cliente:", str(e))



def cadastrar_motocicleta():
    cabeçalho(" Cadastrar Motocicleta ")
    try:
        marca = input("Digite a marca da motocicleta: ").upper()
        modelo = input("Digite o modelo da motocicleta: ").upper()

        # Solicita o ano da motocicleta até que seja digitado um valor numérico
        while True:
            ano = input("Digite o ano da motocicleta: ")
            if ano.isdigit():
                break
            print("Ano inválido. Digite apenas números.")

        # Solicita o preço da motocicleta até que seja digitado um valor numérico
        while True:
            preco = input("Digite o preço da motocicleta: ")
            if preco.isdigit():
                break
            print("Preço inválido. Digite apenas números.")

        with open("motocicletas.txt", "a") as arquivo:
            arquivo.write(f"{marca},{modelo},{ano},{preco}\n")

        print("Motocicleta cadastrada com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao cadastrar a motocicleta:", str(e))
