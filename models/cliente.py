class Cliente:
    def __init__(self, clienteid, cpf, nome, telefone, endereco):
        self.clienteid = clienteid
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
    
    def __repr__(self):
        return f"Cliente ID={self.clienteid}, CPF='{self.cpf}', Nome='{self.nome}', Telefone='{self.telefone}', Endereço='{self.endereco}'"