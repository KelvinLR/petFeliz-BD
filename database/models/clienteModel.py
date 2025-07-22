class Cliente:
    def __init__(self, cliente_id, cpf, nome, telefone, endereco):
        self.cliente_id = cliente_id
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
    
    def __repr__(self):
        return f"Cliente ID={self.cliente_id}, CPF='{self.cpf}', Nome='{self.nome}', Telefone='{self.telefone}', Endereço='{self.endereco}'"