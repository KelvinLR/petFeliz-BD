from database.connection import get_connection
from database.queries.services import Services
from models.funcionario import Funcionario
from models.pet import Pet
from models.cliente import Cliente

select = Services().select

def get_cliente_by_id(clienteid):
    query = "SELECT clienteid, cpf, nome, telefone, endereco FROM Cliente WHERE clienteid = %s;"
    row = select(query=query, params=(clienteid,), fetch='one')

    if row:
        return Cliente(
            clienteid=row[0],
            cpf=row[1],
            nome=row[2],
            telefone=row[3],
            endereco=row[4]
        )
    return None

def get_cliente_by_cpf(clientecpf):
    query = "SELECT clienteid, cpf, nome, telefone, endereco FROM Cliente WHERE cpf = %s;"
    row = select(query=query, params=(clientecpf,), fetch='one')
    
    if row:
        return Cliente(
            clienteid=row[0],
            cpf=row[1],
            nome=row[2],
            telefone=row[3],
            endereco=row[4]
        )
    return None

def get_pet_by_id(petid):
    query = "SELECT petid, nome, idade, datanascimento, raca, especie, clientecpf FROM Pet WHERE petid = %s;"
    row = select(query=query, params=(petid,), fetch='one')
    
    if row:
        return Pet(
            petid=row[0],
            nome=row[1],
            idade=row[2],
            datanascimento=row[3],
            raca=row[4],
            especie=row[5],
            clientecpf=row[6]
        )
    return None

def get_funcionario(funcionarioid: int):
    query = "SELECT funcionarioid, especialidade, nome, salario FROM Funcionario WHERE funcionarioid = %s;"
    row = select(query=query, params=(funcionarioid,),fetch='one')
    
    if row:
        return Funcionario(
            funcionarioid=row[0],
            especialidade=row[1],
            nome=row[2],
            salario=row[3],
        )
    return None

def get_all_clients():
    rows = select(query="SELECT * FROM Cliente;", fetch='all')

    return rows

def get_all_pets():
    rows = select(query="SELECT * FROM Pet;", fetch='all')

    return rows

def get_all_funcionarios():
    rows = select(query="SELECT * FROM Funcionario;", fetch='all')
    
    return rows