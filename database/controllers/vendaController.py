from database.services.vendaService import VendaService
from database.models.vendaModel import Venda

services = VendaService()

class VendaController:
    def venda_create(self):
        print("Digite as informações solicitadas:")
        total_venda = input("Total da venda: ")
        cliente_id = int(input("ID do Cliente: "))
        atendenteid = int(input("ID do Atendente: "))
        id = None

        new_venda = Venda(venda_id=id, total_venda=total_venda, cliente_id=cliente_id, atendente_id=atendenteid)
        services.add(new_venda)

    def update_venda(self):
        print("Digite as informações solicitadas: ")
        venda_id = int(input("Digite o ID da venda que deseja atualizar: "))
        venda = services.get_by_id(venda_id=venda_id)

        if venda is None:
            print("[ERRO] Venda não encontrada")
            return
        
        print(f"Venda atual: {venda}")
        print("Deixe em branco para manter o valor atual")

        total_venda = input(f"Novo total da venda ({venda.total_venda}): ") or venda.total_venda
        cliente_id = input(f"Novo ID do Cliente ({venda.cliente_id}): ") or venda.cliente_id
        atendente_id = input(f"Novo ID do Atendente ({venda.atendente_id}): ") or venda.atendente_id

        venda.total_venda = total_venda
        venda.cliente_id = cliente_id
        venda.atendente_id = atendente_id

        services.update(venda=venda)

    def buscar_venda(self):
        print("\n Digite as informações solicitadas: ")
        venda_id = input("Digite o ID da venda: ")
        venda = services.get_by_id(venda_id)
        if venda:
            print("Venda encontrada:")
            print(venda)
        else:
            print("Venda não encontrada.")

    def remover_venda(self):
        print("\nDigite as informações solicitadas: ")
        venda_id = input("Digite o ID da venda: ")
        venda = services.get_by_id(venda_id=venda_id)

        if venda is None:
            print("[ERRO] Venda não encontrada")
            return
        
        confirm = input(f"Tem certeza que deseja excluir a venda? (s/n): ")
        if confirm.lower() == 's':
            services.delete(vendaid=venda_id)
            print("Venda removida com sucesso")
        else:
            print("Remoção cancelada")

    def listar_vendas(self):
        print("Listando todas as vendas")
        vendas = services.get_all()
        for venda in vendas: #type: ignore
            print(venda)