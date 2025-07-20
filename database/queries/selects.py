from database.connection import get_connection
from models.pet import Pet
from models.cliente import Cliente

def get_cliente_by_id(clienteid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT clienteid, cpf, nome, telefone, endereco FROM Cliente WHERE clienteid = %s;", (clienteid,))
    row = cur.fetchone()
    cur.close()
    conn.close()
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
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT clienteid, cpf, nome, telefone, endereco FROM Cliente WHERE cpf = %s;", (clientecpf,))
    row = cur.fetchone()
    cur.close()
    conn.close()
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
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT petid, nome, idade, datanascimento, raca, especie, clientecpf FROM Pet WHERE petid = %s;", (petid,))
    row = cur.fetchone()
    cur.close()
    conn.close()
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

def get_all_clients():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Cliente;")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    
    return rows

def get_all_pets():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Pet;")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    
    return rows