class Funcionario:
    def __init__(self, funcionario_id, especialidade, nome, salario):
        self.funcionario_id = funcionario_id
        self.especialidade = especialidade
        self.nome = nome
        self.salario = salario

    def __repr__(self):
        return (f"Funcionário ID={self.funcionario_id}, Nome='{self.nome}', Especialidade={self.especialidade}, "
                f"Salário='{self.salario}'")