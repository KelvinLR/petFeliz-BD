from database.connection import get_connection
from models.pet import Pet
from models.cliente import Cliente

def cliente_update(cliente):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Cliente
        SET cpf = %s, nome = %s, telefone = %s, endereco = %s
        WHERE clienteid = %s;
    """, (cliente.cpf, cliente.nome, cliente.telefone, cliente.endereco, cliente.clienteid))
    conn.commit()
    cur.close()
    conn.close()

def pet_update(pet):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Pet
        SET petid = %s, nome = %s, idade = %s, datanascimento = %s, raca = %s, especie = %s, clientecpf = %s
        WHERE petid = %s
    """, (pet.petid, pet.nome, pet.idade, pet.datanascimento, pet.raca, pet.especie, pet.clientecpf))
    conn.commit()
    cur.close()
    conn.close()