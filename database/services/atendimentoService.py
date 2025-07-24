from database.models.atendimentoModel import Atendimento
from database.super_services import SuperServices

execute = SuperServices().execute_query
select = SuperServices().select

class AtendimentoService:
    def get_all(self):
        rows = select(query="SELECT * FROM Atendimento;", fetch='all')
        return [Atendimento(*row) for row in rows]

    def get_by_id(self, atendimento_id):
        query = "SELECT * FROM Atendimento WHERE atendimentoid = %s;"
        row = select(query=query, params=(atendimento_id,), fetch='one')
        if row:
            return Atendimento(*row)
        return None

    def add(self, atendimento: Atendimento):
        query = """
            INSERT INTO Atendimento (dataatendimento, horario, servico, valorcobrado, petid, profissionalid)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING atendimentoid;
        """
        params = (atendimento.data_atendimento, atendimento.horario, atendimento.servico,
                  atendimento.valor_cobrado, atendimento.pet_id, atendimento.profissional_id)
        atendimento.atendimento_id = execute(query=query, params=params, insert=True)
        return atendimento

    def update(self, atendimento: Atendimento):
        query = """
            UPDATE Atendimento
            SET dataatendimento = %s, horario = %s, servico = %s, valorcobrado = %s, petid = %s, profissionalid = %s
            WHERE atendimentoid = %s;
        """
        params = (atendimento.data_atendimento, atendimento.horario, atendimento.servico,
                  atendimento.valor_cobrado, atendimento.pet_id, atendimento.profissional_id, atendimento.atendimento_id)
        execute(query=query, params=params)

    def delete(self, atendimento_id):
        query = "DELETE FROM Atendimento WHERE atendimentoid = %s;"
        execute(query=query, params=(atendimento_id,))