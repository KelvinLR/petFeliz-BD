from datetime import datetime
from database.services.consultaService import ConsultaService
from database.models.consultaModel import Consulta
from database.services.atendimentoService import AtendimentoService
from utils.date_utils import send_date, show_date

service = ConsultaService()

class ConsultaController:
    # def consulta_create(self):
    #     atendimento_id = input("ID do atendimento já existente: ")
    #     motivo = input("Motivo: ")
    #     medicamentos = input("Medicamentos: ")
    #     dataretorno = send_date()
        
    #     if dataretorno is None:
    #         print("Data inválida.")
    #         return

    #     consulta = Consulta(
    #         consulta_id=atendimento_id,  # mesmo valor de AtendimentoID
    #         motivo=motivo,
    #         medicamentos=medicamentos,
    #         dataretorno=dataretorno
    #     )
    #     service.add(consulta)
    def consulta_create(self):
        atendimento_id = input("ID do atendimento já existente (consulta): ")

        atendimento = AtendimentoService().get_by_id(atendimento_id)  # você precisa criar/importar esse método

        if not atendimento:
            print("Atendimento não encontrado.")
            return

        if atendimento.servico != 'Consultas Veterinárias':
            print("O atendimento informado não é do tipo 'Consultas Veterinárias'.")
            return

        motivo = input("Motivo: ")
        medicamentos = input("Medicamentos: ")
        dataretorno = send_date("Data de Retorno (DD/MM/AAAA): ")

        consulta = Consulta(consulta_id=atendimento_id, motivo=motivo, medicamentos=medicamentos, dataretorno=dataretorno)
        service.add(consulta)

        print("Consulta cadastrada com sucesso.")

    def listar_consultas(self):
        consultas = service.get_all()
        for c in consultas:
            c.dataretorno = show_date(c.dataretorno)
            print(c)

    def remover_consulta(self):
        consulta_id = input("ID da consulta a remover: ")
        service.delete(consulta_id)

    def buscar_consulta(self):
        consulta_id = input("ID da consulta: ")
        consulta = service.get_by_id(consulta_id)
        if consulta:
            consulta.dataretorno = show_date(consulta.dataretorno)
            print(consulta)
        else:
            print("Consulta não encontrada.")

    def update_consulta(self):
        consulta_id = input("ID da consulta a atualizar: ")
        consulta = service.get_by_id(consulta_id)
        if not consulta:
            print("Consulta não encontrada.")
            return

        print("Deixe em branco para manter o valor atual.")
        motivo = input(f"Novo Motivo ({consulta.motivo}): ") or consulta.motivo
        medicamentos = input(f"Novo Medicamento ({consulta.medicamentos}): ") or consulta.medicamentos
        nova_dataretorno_input = input(f"Nova Data de Retorno (DD/MM/AAAA) ({show_date(consulta.dataretorno)}): ")
        if nova_dataretorno_input:
            nova_data = send_date(nova_dataretorno_input)
            if nova_data:
                dataretorno = nova_data
            else:
                print("Formato de data inválido. Mantendo a data original.")
                dataretorno = consulta.dataretorno
        else:
            dataretorno = consulta.dataretorno

        consulta.motivo = motivo
        consulta.medicamentos = medicamentos
        consulta.dataretorno = dataretorno

        service.update(consulta)
        print("Consulta atualizada com sucesso.")