class Pet:
    def __init__(self, petid, nome, idade, datanascimento, raca, especie, clientecpf):
        self.petid = petid
        self.nome = nome
        self.idade = idade
        self.datanascimento = datanascimento        
        self.raca = raca
        self.especie = especie
        self.clientecpf = clientecpf

    def __repr__(self):
        return (f"Pet ID={self.petid}, Nome='{self.nome}', Idade={self.idade}, "
                f"Data de Nascimento='{self.datanascimento}', Raça='{self.raca}', "
                f"Espécie='{self.especie}', CPF do Cliente='{self.clientecpf}'")