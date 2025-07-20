from database.connection import get_connection
from models.pet import Pet
from models.cliente import Cliente

def cliente_delete(clienteid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Cliente WHERE clienteid = %s;", (clienteid,))
    conn.commit()
    cur.close()
    conn.close()

def cliente_delete_by_cpf(clientecpf):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Cliente WHERE cpf = %s;", (clientecpf,))
    conn.commit()
    cur.close()
    conn.close()

def pet_delete(petid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Cliente WHERE petid = %s;", (petid,))
    conn.commit()
    cur.close()
    conn.close()