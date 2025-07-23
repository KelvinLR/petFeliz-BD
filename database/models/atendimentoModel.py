class Atendimento:
    def __init__(self, atendimento_id, data_atendimento, horario, servico, pet_id, profissional_id):
        self.atendimento_id = atendimento_id
        self.data_atendimento = data_atendimento
        self.horario = horario
        self.servico = servico
        self.pet_id = pet_id
        self.profissional_id = profissional_id

    def __repr__(self):
        return (f"Atendimento ID={self.atendimento_id}, Data={self.data_atendimento}, "
                f"Horário={self.horario}, Serviço={self.servico}, PetID={self.pet_id}, "
                f"ProfissionalID={self.profissional_id}")