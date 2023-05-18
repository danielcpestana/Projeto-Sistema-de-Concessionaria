from Projeto.lib.interface import *
from Projeto.lib.arquivo import *
arq1 = 'arquivoCliente.txt'
arq2 = 'arquivoProduto.txt'
if not arquivoExisteCliente(arq1):
    criarArquivoCliente(arq1)
if not arquivoExisteProduto(arq2):
    criarArquivoProduto(arq2)
clientes = []
motocicletas = []
vendas = []
while True:
    resp = menu(['Cadastrar Cliente','Cadastrar Motocicleta','Realizar Venda','Listar Vendas','Sair do Sistema'])

    if resp == 1:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('CADASTRO CLIENTE')
        nome = str(input('Nome: '))
        cpf = leiaint('CPF: ')
        cadastrarCliente(arq1, nome, cpf)
        cliente = Cliente(nome, cpf)
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
    elif resp == 2:
        # Opção de cadastrar uma motocicleta
        cabeçalho('CADASTRO MOTOCICLETA')
        marca_motocicleta = input("Digite a marca da motocicleta: ")
        modelo_motocicleta = input("Digite o modelo da motocicleta: ")
        preco_motocicleta = float(input("Digite o preço da motocicleta: "))
        cadastrarProduto(arq2,marca_motocicleta, modelo_motocicleta, preco_motocicleta)
        motocicleta = Motocicleta(marca_motocicleta, modelo_motocicleta, preco_motocicleta)
        motocicletas.append(motocicleta)
        print("Motocicleta cadastrada com sucesso!")


    elif resp == 5:
        cabeçalho('Saindo do sitema...Até logo!')
        break
    else:
        print('\033[31m Erro! Digite uma opção válida!\033[m')
