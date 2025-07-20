from database.connection import get_connection
from models.pet import Pet
from models.cliente import Cliente

def cliente_insert(cliente):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Cliente (cpf, nome, telefone, endereco)
        VALUES (%s, %s, %s, %s)
        RETURNING clienteid;
    """, (cliente.cpf, cliente.nome, cliente.telefone, cliente.endereco))
    cliente.clienteid = cur.fetchone()[0] 
    conn.commit()
    cur.close()
    conn.close()
    return cliente

def pet_insert(pet):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Pet (nome, idade, datanascimento, raca, especie, clientecpf)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING petid;
    """, (pet.nome, pet.idade, pet.datanascimento, pet.raca, pet.especie, pet.clientecpf))
    pet.petid = cur.fetchone()[0]  
    conn.commit()
    cur.close()
    conn.close()
    return pet