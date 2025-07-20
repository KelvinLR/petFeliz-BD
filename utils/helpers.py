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

def update_cliente():
    print("Digite as informações solicitadas")
    clientecpf = input("Digite o CPF do cliente que deseja atualizar: ")
    cliente = get_cliente_by_cpf(clientecpf)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    print(f"Cliente atual: {cliente}")
    print("Deixe em branco para manter o valor atual.")

    cpf = input(f"Novo CPF ({cliente.cpf}): ") or cliente.cpf
    nome = input(f"Novo nome ({cliente.nome}): ") or cliente.nome
    telefone = input(f"Novo telefone ({cliente.telefone}): ") or cliente.telefone
    endereco = input(f"Novo endereço ({cliente.endereco}): ") or cliente.endereco

    cliente.cpf = cpf
    cliente.nome = nome
    cliente.telefone = telefone
    cliente.endereco = endereco

    cliente_update(cliente)

def update_pet():
    print("Digite as informações solicitadas")
    petid = input("Digite o ID do pet que deseja atualizar: ")
    pet = get_pet_by_id(petid)

    if pet is None:
        print("Pet não encontrado.")
        return

    print(f"Pet atual: {pet}")
    print("Deixe em branco para manter o valor atual.")

    nome = input(f"Novo nome ({pet.nome}): ") or pet.nome
    idade = input(f"Nova idade ({pet.idade}): ")
    idade = int(idade) if idade else pet.idade
    datanascimento = input(f"Nova data de nascimento ({pet.datanascimento}): ") or pet.datanascimento
    raca = input(f"Nova raça ({pet.raca}): ") or pet.raca
    especie = input(f"Nova espécie ({pet.especie}): ") or pet.especie
    clientecpf = input(f"Novo CPF do dono ({pet.clientecpf}): ") or pet.clientecpf

    pet.nome = nome
    pet.idade = idade
    pet.datanascimento = datanascimento
    pet.raca = raca
    pet.especie = especie
    pet.clientecpf = clientecpf

    pet_update(pet)

def buscar_cliente():
    print("\nDigite as informações solicitadas")
    clienteid = input("Digite o ID do cliente: ")
    cliente = get_cliente_by_id(clienteid)
    if cliente:
        print("Cliente encontrado:")
        print(cliente)
    else:
        print("Cliente não encontrado.")

def buscar_pet():
    print("\nDigite as informações solicitadas")
    petid = input("Digite o ID do pet: ")
    pet = get_pet_by_id(petid)
    if pet:
        print("Pet encontrado:")
        print(pet)
    else:
        print("Pet não encontrado.")

def remover_pet():
    print("\nDigite as informações solicitadas")
    petid = input("Digite o ID do pet a remover: ")
    pet = get_pet_by_id(petid)
    if pet is None:
        print("Pet não encontrado.")
        return

    confirm = input(f"Tem certeza que deseja remover o pet '{pet.nome}'? (s/n): ")
    if confirm.lower() == 's':
        pet_delete(petid)
        print("Pet removido com sucesso.")
    else:
        print("Remoção cancelada.")

def remover_cliente():
    print("\nDigite as informações solicitadas")
    clientecpf = input("Digite o CPF do cliente a remover: ")
    cliente = get_cliente_by_cpf(clientecpf)
    if cliente is None:
        print("Cliente não encontrado.")
        return

    confirm = input(f"Tem certeza que deseja remover o cliente '{cliente.nome}'? (s/n): ")
    if confirm.lower() == 's':
        cliente_delete_by_cpf(clientecpf)
        print("Cliente removido com sucesso.")
    else:
        print("Remoção cancelada.")

def listar_clientes():
    print('Listando todos os clientes')
    clientes = get_all_clients()
    for cliente in clientes:
        print(cliente)

def listar_pets():
    print('Listando todos os pets')
    pets = get_all_pets()
    for pet in pets:
        print(pet)