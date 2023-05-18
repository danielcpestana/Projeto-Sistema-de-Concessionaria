from Projeto.lib.interface import *

def arquivoExisteCliente(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivoCliente(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivoCliente(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrarCliente(arq1, nome='desconhecido', cpf=0):
    try:
        a = open(arq1, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{cpf}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()




def arquivoExisteProduto(moto):
    try:
        a = open(moto, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivoProduto(moto):
    try:
        a = open(moto, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {moto} criado com sucesso!')


def lerArquivoProduto(moto):
    try:
        a = open(moto, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('MOTOS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrarProduto(arq2, marca_motocicleta='Desconhecido', modelo_motocicleta='Desconhecido', preco_motocicleta='Desconhecido'):
    try:
        a = open(arq2, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{marca_motocicleta};{modelo_motocicleta},{preco_motocicleta}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {marca_motocicleta} adicionado.')
            a.close()


