from database.models.consultaModel import Consulta
from database.super_services import SuperServices

execute = SuperServices().execute_query
select = SuperServices().select

class ConsultaService:
    def get_all(self):
        rows = select(query="SELECT * FROM Consulta;", fetch='all')
        return [Consulta(*row) for row in rows]

    def get_by_id(self, consulta_id):
        query = "SELECT * FROM Consulta WHERE consultaid = %s;"
        row = select(query=query, params=(consulta_id,), fetch='one')
        if row:
            return Consulta(*row)
        return None

    def add(self, consulta: Consulta):
        query = """
            INSERT INTO Consulta (ConsultaID, Motivo, Medicamentos, DataRetorno)
            VALUES (%s, %s, %s, %s);
        """
        params = (consulta.consulta_id, consulta.motivo, consulta.medicamentos, consulta.dataretorno)
        execute(query=query, params=params)
        return consulta

    def update(self, consulta: Consulta):
        query = """
            UPDATE Consulta
            SET motivo = %s, medicamentos = %s, dataretorno = %s
            WHERE consultaid = %s;
        """
        params = (consulta.motivo, consulta.medicamentos, consulta.dataretorno, consulta.consulta_id)
        execute(query=query, params=params)

    def delete(self, consulta_id):
        query = "DELETE FROM Consulta WHERE consultaid = %s;"
        execute(query=query, params=(consulta_id,))

