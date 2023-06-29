import re
from lib.interface.interface import *

def formatar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = re.sub(r'\D', '', cpf)

    # Formata o CPF com pontos e hífen
    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    return cpf_formatado


def validar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito_verificador_1 = 0 if resto < 2 else 11 - resto

    # Verifica o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito_verificador_2 = 0 if resto < 2 else 11 - resto

    # Verifica o segundo dígito verificador
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


def realizar_venda():
    cabeçalho(" Realizar Venda ")
    try:
        listar_motocicletas_disponiveis()
        listar_clientes()

        cpf = input("Digite o CPF do cliente(com os pontos e traços): ")

        # Verifica se o CPF está cadastrado
        if not verificar_cliente_cadastrado(cpf):
            print("CPF não cadastrado. Por favor, verifique o CPF e tente novamente.")
            return

        marca = input("Digite a marca da motocicleta vendida: ").upper()
        modelo = input("Digite o modelo da motocicleta vendida: ").upper()

        # Verifica se a motocicleta está disponível
        if not verificar_motocicleta_disponivel(marca, modelo):
            print("Motocicleta indisponível. Por favor, verifique a marca e o modelo e tente novamente.")
            return

        with open("vendas.txt", "a") as arquivo:
            arquivo.write(f"{cpf},{marca},{modelo}\n")

        print("Venda registrada com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao realizar a venda:", str(e))


def verificar_cliente_cadastrado(cpf):
    with open("clientes.txt", "r") as arquivo:
        clientes = arquivo.readlines()

    for cliente in clientes:
        dados = cliente.strip().split(",")
        if len(dados) == 2 and dados[1] == cpf:
            return True

    return False


def verificar_motocicleta_disponivel(marca, modelo):
    with open("motocicletas.txt", "r") as arquivo_motocicletas, open("vendas.txt", "r") as arquivo_vendas:
        motocicletas = arquivo_motocicletas.readlines()
        vendas = arquivo_vendas.readlines()

    for motocicleta in motocicletas:
        dados = motocicleta.strip().split(",")
        if len(dados) == 4 and dados[0] == marca and dados[1] == modelo:
            for venda in vendas:
                dados_venda = venda.strip().split(",")
                if len(dados_venda) == 3 and dados_venda[1] == marca and dados_venda[2] == modelo:
                    return False
            return True

    return False



def listar_clientes():
    cabeçalho("Clientes Cadastrados ")
    try:
        with open("clientes.txt", "r") as arquivo:
            clientes = arquivo.readlines()

        for cliente in clientes:
            dados = cliente.strip().split(",")
            if len(dados) == 2:
                nome, cpf = dados
                print(f"Nome: {nome}")
                print(f"CPF: {cpf}")
                print("-" * 30)
    except Exception as e:
        print("Ocorreu um erro ao listar os clientes:", str(e))


def listar_motocicletas():
    cabeçalho(" Motocicletas Cadastradas ")
    try:
        with open("motocicletas.txt", "r") as arquivo:
            motocicletas = arquivo.readlines()

        for motocicleta in motocicletas:
            marca, modelo, ano, preco = motocicleta.strip().split(",")
            print(f"Marca: {marca}")
            print(f"Modelo: {modelo}")
            print(f"Ano: {ano}")
            print(f"Preço: {preco}")
            print("-" * 30)
    except Exception as e:
        print("Ocorreu um erro ao listar as motocicletas:", str(e))


def listar_motocicletas_disponiveis():
    cabeçalho(" Motocicletas Disponíveis ")
    try:
        with open("motocicletas.txt", "r") as arquivo_motocicletas, open("vendas.txt", "r") as arquivo_vendas:
            motocicletas = arquivo_motocicletas.readlines()
            vendas = arquivo_vendas.readlines()
        motocicletas_disponiveis = []
        for motocicleta in motocicletas:
            dados_motocicleta = motocicleta.strip().split(",")
            if len(dados_motocicleta) == 4:
                marca, modelo, ano, preco = dados_motocicleta

                vendida = False
                for venda in vendas:
                    dados_venda = venda.strip().split(",")
                    if len(dados_venda) == 3 and dados_venda[1] == marca and dados_venda[2] == modelo:
                        vendida = True
                        break
                if not vendida:
                    motocicletas_disponiveis.append(motocicleta)

        for motocicleta in motocicletas_disponiveis:
            marca, modelo, ano, preco = motocicleta.strip().split(",")
            print(f"Marca: {marca}")
            print(f"Modelo: {modelo}")
            print(f"Ano: {ano}")
            print(f"Preço: {preco}")
            print("-" * 30)
    except Exception as e:
        print("Ocorreu um erro ao listar as motocicletas disponíveis:", str(e))


def listar_vendas():
    cabeçalho(" Vendas Realizadas ")
    try:
        with open("vendas.txt", "r") as arquivo:
            vendas = arquivo.readlines()

        for venda in vendas:
            dados_venda = venda.strip().split(",")
            if len(dados_venda) == 3:
                cpf, marca, modelo = dados_venda

                cpf_formatado = formatar_cpf(cpf)  # Formata o CPF

                print(f"CPF do cliente: {cpf_formatado}")
                print(f"Marca da motocicleta: {marca}")
                print(f"Modelo da motocicleta: {modelo}")

                print("-" * 30)
    except Exception as e:
        print("Ocorreu um erro ao listar as vendas:", str(e))

