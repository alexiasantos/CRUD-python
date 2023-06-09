"""
Faça uma lista de compras com listas. O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os
from time import sleep
import sys


def inserir(list):
    os.system('cls')
    item = str(input(f'Digite o nome do item a ser inserido: '))
    list.append(item)
    print(f'{"LISTA ALTERADA":^20}')
    listar(list)


def editar(list):
    listar(list)
    while True:
        item = int(input(f'Qual valor deseja editar de 0 a {len(list)-1}:'))
        for pos, i in enumerate(list):
            if pos == item:
                list[item] = str(input('Digite o novo valor: '))
                print(f'{"LISTA ALTERADA":^20}')
                listar(list)
                return 0
        else:
            print('Este valor não existe, tente novamente!!!!')
            sleep(2)


def apagar(list):
    os.system('cls')
    listar(list)
    try:
        item = int(
            input(f'Qual item voce deseja apagar ? de 0 a {len(list)}: '))
        list.pop(item)
    except ValueError:
        print('Por favor digite número int.')
        sleep(2)
    except IndexError:
        print('Índice não existe na lista')
        sleep(2)
    except Exception:
        print('Erro desconhecido')
        sleep(2)
    os.system('cls')
    print(f'{"LISTA ALTERADA":^20}')
    listar(list)
    sleep(1)


def listar(list):
    os.system('cls')
    for pos, item in enumerate(list):
        print(f'{pos} - {item}')
    sleep(1)


def menu():
    print()
    print(f'{"LISTA DE COMPRAS":^20}')
    print('\t 1 - Ver lista')
    print('\t 2 - Apagar')
    print('\t 3 - Inserir')
    print('\t 4 - Editar')
    print('\t 5 - Sair')


def sair():
    sys.exit()


# programa principal
Lista_compras = []
while True:
    menu()
    opcao = int(input('Opção: '))
    if opcao == 1:
        os.system('cls')
        listar(Lista_compras)
    elif opcao == 2:
        os.system('cls')
        apagar(Lista_compras)
    elif opcao == 3:
        os.system('cls')
        inserir(Lista_compras)
    elif opcao == 4:
        os.system('cls')
        editar(Lista_compras)
    elif opcao == 5:
        print(f'{"FINALIZANDO.....":^20}')
        sleep(1)
        sair()
    else:
        print('Opção inválida digite novamente')
        os.system('cls')
        continue
