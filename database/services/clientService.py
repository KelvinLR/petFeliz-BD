from database.super_services import SuperServices
from database.models.clienteModel import Cliente


execute = SuperServices().execute_query
select = SuperServices().select

class ClientService:
    def get_all(self):
        rows = select(query="SELECT * FROM Cliente;", fetch='all')

        return rows

    def get_by_id(self, cliente_id):
        query = "SELECT clienteid, cpf, nome, telefone, endereco FROM Cliente WHERE clienteid = %s;"
        row = select(query=query, params=(cliente_id,), fetch='one')

        if row:
            return Cliente(
                cliente_id=row[0],
                cpf=row[1],
                nome=row[2],
                telefone=row[3],
                endereco=row[4]
            )
        return None

    def get_by_cpf(self, cliente_cpf):
        query = "SELECT clienteid, cpf, nome, telefone, endereco FROM Cliente WHERE cpf = %s;"
        row = select(query=query, params=(cliente_cpf,), fetch='one')
        
        if row:
            return Cliente(
                cliente_id=row[0],
                cpf=row[1],
                nome=row[2],
                telefone=row[3],
                endereco=row[4]
            )
        return None

    def add(self, cliente: Cliente):
        query = """
            INSERT INTO Cliente (cpf, nome, telefone, endereco)
            VALUES (%s, %s, %s, %s)
            RETURNING clienteid;
        """
        params = (cliente.cpf, cliente.nome, cliente.telefone, cliente.endereco)
        
        cliente.cliente_id = execute(query=query, params=params, insert=True)

        return cliente

    def delete(self, clienteid):
        query = "DELETE FROM Cliente WHERE clienteid = %s;"
        execute(query=query, params=(clienteid,))

    def delete_by_cpf(self, clientecpf):
        query = "DELETE FROM Cliente WHERE cpf = %s;"
        execute(query=query, params=(clientecpf,))

    def update(self, cliente: Cliente):
        query = """
            UPDATE Cliente
            SET cpf = %s, nome = %s, telefone = %s, endereco = %s
            WHERE clienteid = %s;
        """
        params = (cliente.cpf, cliente.nome, cliente.telefone, cliente.endereco, cliente.cliente_id)

        execute(query=query, params=params)