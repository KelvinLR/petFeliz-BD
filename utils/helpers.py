from models.pet import Pet
from models.cliente import Cliente
from database.queries.inserts import *
from database.queries.deletes import *
from database.queries.updates import *
from database.queries.selects import *

def menu():
    while True:
        print("\n=== PetShop PetFeliz ===")
        print("1 - Operar Cliente")
        print("2 - Operar Pet")
        print("3 - Sair")
        op = input("Escolha uma opção: ")

        if op == '1':
            while True:
                print("\n-- Menu Cliente --")
                print("1 - Inserir Cliente")
                print("2 - Atualizar Cliente")
                print("3 - Buscar Cliente")
                print("4 - Remover Cliente")
                print("5 - Voltar ao menu principal")
                opcao_cliente = input("Escolha uma opção: ")

                if opcao_cliente == '1':
                    print("Inserir Cliente selecionado")
                elif opcao_cliente == '2':
                    print("Atualizar Cliente selecionado")
                elif opcao_cliente == '3':
                    print("Buscar Cliente selecionado")
                elif opcao_cliente == '4':
                    print("Remover Cliente selecionado")
                elif opcao_cliente == '5':
                    break
                else:
                    print("Opção inválida, tente novamente.")

        elif op == '2':
            while True:
                print("\n-- Menu Pet --")
                print("1 - Inserir Pet")
                print("2 - Atualizar Pet")
                print("3 - Buscar Pet")
                print("4 - Remover Pet")
                print("5 - Voltar ao menu principal")
                opcao_pet = input("Escolha uma opção: ")

                if opcao_pet == '1':
                    print("Inserir Pet selecionado")
                elif opcao_pet == '2':
                    print("Atualizar Pet selecionado")
                elif opcao_pet == '3':
                    print("Buscar Pet selecionado")
                elif opcao_pet == '4':
                    print("Remover Pet selecionado")
                elif opcao_pet == '5':
                    break
                else:
                    print("Opção inválida, tente novamente.")

        elif op == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def client_create():
    print("Digite as informações solicitadas")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    id = None

    new_cliente = Cliente(id, cpf, nome, telefone, endereco)
    cliente_insert(new_cliente)


def pet_create():
    print("Digite as informações solicitadas")
    clientecpf = input("CPF do Cliente: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    datanascimento = input("Data de Nascimento: ")
    raca = input("Raça: ")
    especie = input("Espécie: ")
    id = None

    new_pet = Pet(id,nome, idade, datanascimento, raca, especie, clientecpf)
    pet_insert(new_pet)