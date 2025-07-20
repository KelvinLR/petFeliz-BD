from database.super_services import SuperServices
from database.models.funcionarioModel import Funcionario


execute = SuperServices().execute_query
select = SuperServices().select

class FuncionarioService:
    def get_all_funcionarios(self):
        rows = select(query="SELECT * FROM Funcionario;", fetch='all')
        
        return rows
    def get_by_id(self, funcionario_id: int):
        query = "SELECT funcionarioid, especialidade, nome, salario FROM Funcionario WHERE funcionarioid = %s;"
        row = select(query=query, params=(funcionario_id,),fetch='one')
        
        if row:
            return Funcionario(
                funcionario_id=row[0],
                especialidade=row[1],
                nome=row[2],
                salario=row[3],
            )
        return None

    def add(self, funcionario: Funcionario):
        query = """
            INSERT INTO Funcionario (especialidade, nome, salario)
            VALUES (%s, %s, %s)
            RETURNING funcionarioid;
        """
        params = (funcionario.especialidade, funcionario.nome, funcionario.salario)
        funcionario.funcionario_id = execute(query=query, params=params, insert=True)

        return funcionario

    def funcionario_delete(self, funcionario_id):
        query = "DELETE FROM Funcionario WHERE funcionarioid = %s;"
        execute(query=query, params=(funcionario_id,))

    def funcionario_update(self, funcionario: Funcionario):
        query = """
            UPDATE Funcionario
            SET nome = %s, especialidade = %s, salario = %s
            WHERE funcionarioid = %s
        """
        params = (funcionario.nome, funcionario.especialidade, funcionario.salario, funcionario.funcionario_id, )
        
        execute(query=query, params=params)