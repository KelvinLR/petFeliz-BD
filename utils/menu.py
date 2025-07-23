from database.controllers.clientController import ClientController
from database.controllers.funcionarioController import FuncionarioController
from database.controllers.petController import PetController
from database.controllers.produtoController import ProdutoController
from database.controllers.atendimentoController import AtendimentoController
from database.controllers.consultaController import ConsultaController

def menu():
    while True:
        print("\n=== PetShop PetFeliz ===")
        print("1 - Operar Cliente")
        print("2 - Operar Pet")
        print("3 - Funcionario")
        print("4 - Produto")
        print("5 - Atendimento")
        print("6 - Consulta")
        print("0 - Sair")
        op = input("Escolha uma opção: ")

        if op == '1':
            while True:
                print("\n-- Menu Cliente --")
                print("1 - Inserir Cliente")
                print("2 - Atualizar Cliente")
                print("3 - Buscar Cliente")
                print("4 - Remover Cliente")
                print("5 - Listar todos os clientes")
                print("0 - Voltar ao menu principal")
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
                elif opcao_cliente == '0':
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
                print("0 - Voltar ao menu principal")
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
                elif opcao_pet == '0':
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif op == '3':
            while True:
                print("\n-- Menu Funcionario --")
                print("1 - Inserir funcionario")
                print("2 - Atualizar funcionario")
                print("3 - Buscar funcionario")
                print("4 - Remover funcionario")
                print("5 - Listar todos os funcionarios")
                print("0 - Voltar ao menu principal")
                opcao_funcionario = input("Escolha uma opção: ")

                if opcao_funcionario == '1':
                    print("Inserir Funcionario selecionado")
                    funcionario_create()
                elif opcao_funcionario == '2':
                    print("Atualizar Funcionario selecionado")
                    update_funcionario()
                elif opcao_funcionario == '3':
                    print("Buscar Funcionario selecionado")
                    buscar_funcionario()
                elif opcao_funcionario == '4':
                    print("Remover Funcionario selecionado")
                    remover_funcionario()
                elif opcao_funcionario == '5':
                    listar_funcionario()
                elif opcao_funcionario == '0':
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif op == '4':
            while True:
                print("\n-- Menu Produto --")
                print("1 - Inserir produto")
                print("2 - Atualizar produto")
                print("3 - Buscar produto")
                print("4 - Remover produto")
                print("5 - Listar todos os produtos")
                print("0 - Voltar ao menu principal")
                opcao_produto = input("Escolha uma opção: ")

                if opcao_produto == '1':
                    print("Inserir Produto selecionado")
                    produto_create()
                elif opcao_produto == '2':
                    print("Atualizar Produto selecionado")
                    update_produto()
                elif opcao_produto == '3':
                    print("Buscar Produto selecionado")
                    buscar_produto()
                elif opcao_produto == '4':
                    print("Remover Produto selecionado")
                    remover_produto()
                elif opcao_produto == '5':
                    listar_produto()
                elif opcao_produto == '0':
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif op == '5':
            while True:
                print("\n-- Menu Atendimento --")
                print("1 - Inserir Atendimento")
                print("2 - Atualizar Atendimento")
                print("3 - Buscar Atendimento")
                print("4 - Remover Atendimento")
                print("5 - Listar Atendimentos")
                print("0 - Voltar ao menu principal")
                opcao_atendimento = input("Escolha uma opção: ")

                if opcao_atendimento == '1':
                    atendimento_create()
                elif opcao_atendimento == '2':
                    update_atendimento()
                elif opcao_atendimento == '3':
                    buscar_atendimento()
                elif opcao_atendimento == '4':
                    remover_atendimento()
                elif opcao_atendimento == '5':
                    listar_atendimentos()
                elif opcao_atendimento == '0':
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif op == '6':
            while True:
                print("\n-- Menu Consulta --")
                print("1 - Inserir Consulta")
                print("2 - Atualizar Consulta")
                print("3 - Buscar Consulta")
                print("4 - Remover Consulta")
                print("5 - Listar Consultas")
                print("0 - Voltar ao menu principal")
                opcao_consulta = input("Escolha uma opção: ")

                if opcao_consulta == '1':
                    consulta_create()
                elif opcao_consulta == '2':
                    update_consulta()
                elif opcao_consulta == '3':
                    buscar_consulta()
                elif opcao_consulta == '4':
                    remover_consulta()
                elif opcao_consulta == '5':
                    listar_consultas()
                elif opcao_consulta == '0':
                    break
                else:
                    print("Opção inválida, tente novamente.")
        elif op == '0':
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

def funcionario_create():
    FuncionarioController().funcionario_create()
def update_funcionario():
    FuncionarioController().update_funcionario()
def buscar_funcionario():
    FuncionarioController().buscar_funcionario()
def remover_funcionario():
    FuncionarioController().remover_funcionario()
def listar_funcionario():
    FuncionarioController().listar_funcionarios()

def produto_create():
    ProdutoController().produto_create()
def update_produto():
    ProdutoController().update_produto()
def buscar_produto():
    ProdutoController().buscar_produto()
def remover_produto():
    ProdutoController().remover_produto()
def listar_produto():
    ProdutoController().listar_produtos()

def atendimento_create():
    AtendimentoController().atendimento_create()
def update_atendimento():
    AtendimentoController().update_atendimento()
def buscar_atendimento():
    AtendimentoController().buscar_atendimento()
def remover_atendimento():
    AtendimentoController().remover_atendimento()
def listar_atendimentos():
    AtendimentoController().listar_atendimentos()


def consulta_create():
    ConsultaController().consulta_create()
def update_consulta():
    ConsultaController().update_consulta()
def buscar_consulta():
    ConsultaController().buscar_consulta()
def remover_consulta():
    ConsultaController().remover_consulta()
def listar_consultas():
    ConsultaController().listar_consultas()