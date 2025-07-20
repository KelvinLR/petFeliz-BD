from database.controllers.clientController import ClientController
from database.controllers.petController import PetController

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
                print("5 - Listar todos os clientes")
                print("6 - Voltar ao menu principal")
                opcao_cliente = input("Escolha uma opção: ")

                if opcao_cliente == '1':
                    print("Inserir Cliente selecionado")
                    client_create()
                elif opcao_cliente == '2':
                    print("Atualizar Cliente selecionado")
                    update_cliente()
                elif opcao_cliente == '3':
                    print("Buscar Cliente selecionado")
                    buscar_cliente()
                elif opcao_cliente == '4':
                    print("Remover Cliente selecionado")
                    remover_cliente()
                elif opcao_cliente == '5':
                    listar_clientes()
                elif opcao_cliente == '6':
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
                print("5 - Listar todos os pets")
                print("6 - Voltar ao menu principal")
                opcao_pet = input("Escolha uma opção: ")

                if opcao_pet == '1':
                    print("Inserir Pet selecionado")
                    pet_create()
                elif opcao_pet == '2':
                    print("Atualizar Pet selecionado")
                    update_pet()
                elif opcao_pet == '3':
                    print("Buscar Pet selecionado")
                    buscar_pet()
                elif opcao_pet == '4':
                    print("Remover Pet selecionado")
                    remover_pet()
                elif opcao_pet == '5':
                    listar_pets()
                elif opcao_pet == '6':
                    break
                else:
                    print("Opção inválida, tente novamente.")

        elif op == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def client_create():
    ClientController().client_create()
def update_cliente():
    ClientController().update_cliente()
def buscar_cliente():
    ClientController().buscar_cliente()
def remover_cliente():
    ClientController().remover_cliente()
def listar_clientes():
    ClientController().listar_clientes()

def pet_create():
    PetController().pet_create()
def update_pet():
    PetController().update_pet()
def buscar_pet():
    PetController().buscar_pet()
def remover_pet():
    PetController().remover_pet()
def listar_pets():
    PetController().listar_pets()