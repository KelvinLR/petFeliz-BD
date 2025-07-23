from datetime import datetime
from database.models.atendimentoModel import Atendimento
from database.services.atendimentoService import AtendimentoService
from utils.date_utils import send_date, show_date

services = AtendimentoService()

class AtendimentoController:
    def atendimento_create(self):
        print("Digite os dados do atendimento")
        data = send_date("Data (DD/MM/AAAA): ")
        if data is None:
            return
        horario = input("Horário (HH:MM): ")
        servico = input("Serviço ('Consultas Veterinárias' ou 'Banho e Tosa'): ")
        pet_id = int(input("ID do Pet: "))
        profissional_id = int(input("ID do Profissional: "))
        id = None

        novo_atendimento = Atendimento(id, data, horario, servico, pet_id, profissional_id)
        services.add(novo_atendimento)

    def listar_atendimentos(self):
        print("Listando atendimentos")
        atendimentos = services.get_all()
        for a in atendimentos:
            a.data_atendimento = show_date(a.data_atendimento)
            print(a)

    def remover_atendimento(self):
        atendimento_id = input("Digite o ID do atendimento a remover: ")
        services.delete(atendimento_id)
        print("Atendimento removido com sucesso.")

    def buscar_atendimento(self):
        atendimento_id = input("Digite o ID do atendimento: ")
        atendimento = services.get_by_id(atendimento_id)
        if atendimento:
            print("Atendimento encontrado:")
            print(atendimento)
        else:
            print("Atendimento não encontrado.")

    def update_atendimento(self):
        atendimento_id = input("Digite o ID do atendimento que deseja atualizar: ")
        atendimento = services.get_by_id(atendimento_id)

        if atendimento is None:
            print("Atendimento não encontrado.")
            return

        print(f"Atendimento atual: {atendimento}")
        print("Deixe em branco para manter o valor atual.")

        nova_data = input(f"Nova Data (DD/MM/AAAA) ({show_date(atendimento.data_atendimento)}): ")
        if nova_data:
            try:
                data = datetime.strptime(nova_data, "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")
                return
        else:
            data = atendimento.data_atendimento
        horario = input(f"Novo Horário ({atendimento.horario}): ") or atendimento.horario
        servico = input(f"Novo Serviço ({atendimento.servico}): ") or atendimento.servico
        pet_id = input(f"Novo Pet ID ({atendimento.pet_id}): ") or atendimento.pet_id
        profissional_id = input(f"Novo Profissional ID ({atendimento.profissional_id}): ") or atendimento.profissional_id

        atendimento.data_atendimento = data
        atendimento.horario = horario
        atendimento.servico = servico
        atendimento.pet_id = int(pet_id)
        atendimento.profissional_id = int(profissional_id)

        services.update(atendimento)
        print("Atendimento atualizado com sucesso.")