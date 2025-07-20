from database.connection import get_connection
from database.queries.services import Services
from models.funcionario import Funcionario
from models.pet import Pet
from models.cliente import Cliente

insert = Services().execute_query

def cliente_insert(cliente: Cliente):
    query = """
        INSERT INTO Cliente (cpf, nome, telefone, endereco)
        VALUES (%s, %s, %s, %s)
        RETURNING clienteid;
    """
    params = (cliente.cpf, cliente.nome, cliente.telefone, cliente.endereco)
    
    cliente.clienteid = insert(query=query, params=params, insert=True)

    return cliente

def pet_insert(pet: Pet):
    query = """
        INSERT INTO Pet (nome, idade, datanascimento, raca, especie, clientecpf)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING petid;
    """
    params = (pet.nome, pet.idade, pet.datanascimento, pet.raca, pet.especie, pet.clientecpf)
    pet.petid = insert(query=query, params=params, insert=True)

    return pet

def funcionario_insert(funcionario: Funcionario):
    query = """
        INSERT INTO Funcionario (especialidade, nome, salario)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING FuncionarioID;
    """
    params = (funcionario.especialidade, funcionario.nome, funcionario.salario)
    funcionario.funcionarioid = insert(query=query, params=params, insert=True)

    return funcionario
