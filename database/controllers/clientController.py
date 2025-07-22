from database.services.clientService import ClientService
from database.models.clienteModel import Cliente

services = ClientService()

class ClientController:
    def client_create(self):
        print("Digite as informações solicitadas")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        id = None

        new_cliente = Cliente(id, cpf, nome, telefone, endereco)
        services.add(new_cliente)

    def update_cliente(self):
        print("Digite as informações solicitadas")
        clientecpf = input("Digite o CPF do cliente que deseja atualizar: ")
        cliente = services.get_by_cpf(clientecpf)

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

        services.update(cliente)

    def buscar_cliente(self):
        print("\nDigite as informações solicitadas")
        clienteid = input("Digite o ID do cliente: ")
        cliente = services.get_by_id(clienteid)
        if cliente:
            print("Cliente encontrado:")
            print(cliente)
        else:
            print("Cliente não encontrado.")
    
    def remover_cliente(self):
        print("\nDigite as informações solicitadas")
        clientecpf = input("Digite o CPF do cliente a remover: ")
        cliente = services.get_by_cpf(clientecpf)
        if cliente is None:
            print("Cliente não encontrado.")
            return

        confirm = input(f"Tem certeza que deseja remover o cliente '{cliente.nome}'? (s/n): ")
        if confirm.lower() == 's':
            services.delete_by_cpf(clientecpf)
            print("Cliente removido com sucesso.")
        else:
            print("Remoção cancelada.")

    def listar_clientes(self):
        print('Listando todos os clientes')
        clientes = services.get_all()
        for cliente in clientes: # type: ignore
            print(cliente)