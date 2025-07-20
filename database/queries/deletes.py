from database.queries.services import Services
from models.pet import Pet
from models.cliente import Cliente

delete = Services().execute_query

def cliente_delete(clienteid):
    query = "DELETE FROM Cliente WHERE clienteid = %s;"
    delete(query=query, params=(clienteid,))

def cliente_delete_by_cpf(clientecpf):
    query = "DELETE FROM Cliente WHERE cpf = %s;"
    delete(query=query, params=(clientecpf,))

def cliente_delete_by_cpf(clientecpf):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Cliente WHERE cpf = %s;", (clientecpf,))
    conn.commit()
    cur.close()
    conn.close()

def pet_delete(petid):
    query = "DELETE FROM Pet WHERE petid = %s;"
    delete(query=query, params=(petid,))

def funcionario_delete(funcionarioid):
    query = "DELETE FROM Funcionario WHERE funcionarioid = %s;"
    delete(query=query, params=(funcionarioid,))