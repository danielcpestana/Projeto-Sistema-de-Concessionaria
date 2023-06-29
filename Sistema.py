from lib.arquivos.arquivo import *
from lib.interface.interface import *


while True:
    resp = menu(['Cadastrar Cliente','Cadastrar Motocicleta','Realizar Venda','Listar Clientes','Listar Motocicletas Disponíveis','Listar Vendas','Sair do Sistema'])
    if resp == 1:
        cadastrar_cliente()
    elif resp == 2:
        # Opção de cadastrar uma motocicleta
        cadastrar_motocicleta()
    elif resp == 3:
        # Opção de realizar uma venda
        realizar_venda()
    elif resp == 4:
        listar_clientes()
    elif resp == 5:
        listar_motocicletas_disponiveis()
    elif resp == 6:
        listar_vendas()
    elif resp == 7:
        break
    else:
        print('\033[31m Erro! Digite uma opção válida!\033[m')
