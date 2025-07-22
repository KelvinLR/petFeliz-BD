from database.super_services import SuperServices
from database.models.petModel import Pet


execute = SuperServices().execute_query
select = SuperServices().select

class PetService:
    def get_all_pets(self):
        rows = select(query="SELECT * FROM Pet;", fetch='all')

        return rows

    def get_by_id(self, pet_id):
        query = "SELECT petid, nome, idade, datanascimento, raca, especie, clientecpf FROM Pet WHERE petid = %s;"
        row = select(query=query, params=(pet_id,), fetch='one')
        
        if row:
            return Pet(
                pet_id=row[0],
                nome=row[1],
                idade=row[2],
                data_nascimento=row[3],
                raca=row[4],
                especie=row[5],
                cliente_cpf=row[6]
            )
        return None
    
    
    def add(self, pet: Pet):
        query = """
            INSERT INTO Pet (nome, idade, datanascimento, raca, especie, clientecpf)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING petid;
        """
        params = (pet.nome, pet.idade, pet.data_nascimento, pet.raca, pet.especie, pet.cliente_cpf)
        pet.pet_id = execute(query=query, params=params, insert=True)

        return pet
    
    def update(self, pet: Pet):
        query = """
            UPDATE Pet
            SET nome = %s, idade = %s, datanascimento = %s, raca = %s, especie = %s, clientecpf = %s
            WHERE petid = %s
        """
        params = (pet.nome, pet.idade, pet.data_nascimento, pet.raca, pet.especie, pet.cliente_cpf, pet.pet_id)
        
        execute(query=query, params=params)

    def delete(self, petid):
        query = "DELETE FROM Pet WHERE petid = %s;"
        execute(query=query, params=(petid,))
