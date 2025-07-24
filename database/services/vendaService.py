from database.super_services import SuperServices
from database.models.vendaModel import Venda

execute = SuperServices().execute_query
select = SuperServices().select

class VendaService:
    def get_all(self):
        rows = select(query="SELECT * FROM Venda;", fetch='all')

        return rows
    
    def get_by_id(self, venda_id):
        query = "SELECT vendaid, totalvenda, clienteid, atendenteid FROM Venda WHERE vendaid = %s;"
        row = select(query=query, params=(venda_id,),fetch='one')

        if row:
            return Venda(
                venda_id=row[0],
                total_venda=row[1],
                cliente_id=row[2],
                atendente_id=row[3]
            )
        return None
    
    def add(self, venda: Venda):
        query = """
            INSERT INTO Venda (totalvenda, clienteid, atendenteid)
            VALUES (%s,%s,%s)
            RETURNING vendaid
        """
        params = (venda.total_venda, venda.cliente_id, venda.atendente_id)
        venda.venda_id = execute(query=query, params=params, insert=True)

        return venda
    
    def delete(self, vendaid):
        query = "DELETE FROM Venda WHERE vendaid = %s;"
        execute(query=query, params=(vendaid,))

    def update(self, venda: Venda):
        query = """
            UPDATE Venda
            SET totalvenda = %s, clienteid = %s, atendenteid = %s
            WHERE vendaid = %s
        """
        params = (venda.total_venda, venda.cliente_id, venda.atendente_id, venda.venda_id)

        execute(query=query, params=params)