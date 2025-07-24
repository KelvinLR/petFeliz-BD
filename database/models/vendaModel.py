class Venda:
    def __init__(self, venda_id, total_venda, cliente_id, atendente_id):
        self.venda_id = venda_id
        self.total_venda = total_venda
        self.cliente_id = cliente_id    
        self.atendente_id = atendente_id
        
    def __repr__(self):
        return (f"Venda ID={self.venda_id}, Total da Venda='{self.total_venda}', Cliente ID={self.cliente_id}, "
                f"Atendente ID='{self.atendente_id}'")