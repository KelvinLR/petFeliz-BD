class Pet:
    def __init__(self, pet_id, nome, idade, data_nascimento, raca, especie, cliente_cpf):
        self.pet_id = pet_id
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento        
        self.raca = raca
        self.especie = especie
        self.cliente_cpf = cliente_cpf

    def __repr__(self):
        return (f"Pet ID={self.pet_id}, Nome='{self.nome}', Idade={self.idade}, "
                f"Data de Nascimento='{self.data_nascimento}', Raça='{self.raca}', "
                f"Espécie='{self.especie}', CPF do Cliente='{self.cliente_cpf}'")