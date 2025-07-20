from database.queries.services import Services
from models.funcionario import Funcionario
from models.pet import Pet
from models.cliente import Cliente

update = Services().execute_query

def cliente_update(cliente: Cliente):
    query = """
        UPDATE Cliente
        SET cpf = %s, nome = %s, telefone = %s, endereco = %s
        WHERE clienteid = %s;
    """
    params = (cliente.cpf, cliente.nome, cliente.telefone, cliente.endereco, cliente.clienteid)

    update(query=query, params=params)

def pet_update(pet: Pet):
    query = """
        UPDATE Pet
        SET nome = %s, idade = %s, datanascimento = %s, raca = %s, especie = %s, clientecpf = %s
        WHERE petid = %s
    """
    params = (pet.nome, pet.idade, pet.datanascimento, pet.raca, pet.especie, pet.clientecpf, pet.petid)
    
    update(query=query, params=params)

def funcionario_update(funcionario: Funcionario):
    query = """
        UPDATE Funcionario
        SET nome = %s, especialidade = %s, nome = %s, salario = %s
        WHERE funcionarioid = %s
    """
    params = (funcionario.nome, funcionario.especialidade, funcionario.salario, funcionario.funcionarioid, )
    
    update(query=query, params=params)