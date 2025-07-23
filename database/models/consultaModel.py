class Consulta:
    def __init__(self, consulta_id, motivo, medicamentos, dataretorno):
        self.consulta_id = consulta_id
        self.motivo = motivo
        self.medicamentos = medicamentos
        self.dataretorno = dataretorno

    def __repr__(self):
        return (f"Consulta ID={self.consulta_id}, Motivo='{self.motivo}', "
                f"Medicamentos='{self.medicamentos}', Data de Retorno={self.dataretorno}")