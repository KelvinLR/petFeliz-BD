from database.services.funcionarioService import FuncionarioService
from database.models.funcionarioModel import Funcionario

services = FuncionarioService()

class FuncionarioController:
    def funcionario_create(self):
        print("Digite as informações solicitadas")
        especialidade = input("Especialidade: ")
        nome = input("Nome: ")
        salario = input("Salário: ")
        id = None

        new_funcionario = Funcionario(funcionario_id=id, especialidade=especialidade, nome=nome, salario=salario)
        services.add(new_funcionario)

    def update_funcionario(self):
        print("Digite as informações solicitadas")
        funcionario_id = input("Digite o ID do funcionário que deseja atualizar: ")
        funcionario = services.get_by_id(funcionario_id)

        if funcionario is None:
            print("Funcionário não encontrado.")
            return

        print(f"Funcionário atual: {funcionario}")
        print("Deixe em branco para manter o valor atual.")

        especialidade = input(f"Nova especialidade ({funcionario.especialidade}): ") or funcionario.especialidade
        nome = input(f"Novo nome ({funcionario.nome}): ") or funcionario.nome
        salario = input(f"Novo salário ({funcionario.salario}): ") or funcionario.salario

        funcionario.especialidade = especialidade
        funcionario.nome = nome
        funcionario.salario = salario

        services.update(funcionario)

    def buscar_funcionario(self):
        print("\nDigite as informações solicitadas")
        funcionario_id = input("Digite o ID do funcionário: ")
        funcionario = services.get_by_id(funcionario_id)
        if funcionario:
            print("Funcionário encontrado:")
            print(funcionario)
        else:
            print("Funcionário não encontrado.")
    
    def remover_funcionario(self):
        print("\nDigite as informações solicitadas")
        funcionario_id = input("Digite o ID do funcionário: ")
        funcionario = services.get_by_id(funcionario_id)

        if funcionario is None:
            print("Funcionário não encontrado.")
            return
            
        confirm = input(f"Tem certeza que deseja remover o funcionário '{funcionario.nome}'? (s/n): ")
        if confirm.lower() == 's':
            services.delete(funcionario_id)
            print("Funcionário removido com sucesso.")
        else:
            print("Remoção cancelada.")

    def listar_funcionarios(self):
        print('Listando todos os funcionários')
        funcionarios = services.get_all()
        for funcionario in funcionarios: # type: ignore
            print(funcionario)