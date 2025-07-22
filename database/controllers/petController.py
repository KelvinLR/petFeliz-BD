from database.services.petService import PetService
from database.models.petModel import Pet


services = PetService()

class PetController:
    def pet_create(self):
        print("Digite as informações solicitadas")
        clientecpf = input("CPF do Cliente: ")
        nome = input("Nome: ")
        idade = input("Idade: ")
        datanascimento = input("Data de Nascimento: ")
        raca = input("Raça: ")
        especie = input("Espécie: ")
        id = None

        new_pet = Pet(id,nome, idade, datanascimento, raca, especie, clientecpf)
        services.add(new_pet)

    def update_pet(self):
        print("Digite as informações solicitadas")
        petid = input("Digite o ID do pet que deseja atualizar: ")
        pet = services.get_by_id(petid)

        if pet is None:
            print("Pet não encontrado.")
            return

        print(f"Pet atual: {pet}")
        print("Deixe em branco para manter o valor atual.")

        nome = input(f"Novo nome ({pet.nome}): ") or pet.nome
        idade = input(f"Nova idade ({pet.idade}): ")
        idade = int(idade) if idade else pet.idade
        datanascimento = input(f"Nova data de nascimento ({pet.data_nascimento}): ") or pet.data_nascimento
        raca = input(f"Nova raça ({pet.raca}): ") or pet.raca
        especie = input(f"Nova espécie ({pet.especie}): ") or pet.especie
        clientecpf = input(f"Novo CPF do dono ({pet.cliente_cpf}): ") or pet.cliente_cpf

        pet.nome = nome
        pet.idade = idade
        pet.data_nascimento = datanascimento
        pet.raca = raca
        pet.especie = especie
        pet.cliente_cpf = clientecpf

        services.update(pet)

    def buscar_pet(self):
        print("\nDigite as informações solicitadas")
        petid = input("Digite o ID do pet: ")
        pet = services.get_by_id(petid)
        if pet:
            print("Pet encontrado:")
            print(pet)
        else:
            print("Pet não encontrado.")

    def remover_pet(self):
        print("\nDigite as informações solicitadas")
        petid = input("Digite o ID do pet a remover: ")
        pet = services.get_by_id(petid)
        if pet is None:
            print("Pet não encontrado.")
            return

        confirm = input(f"Tem certeza que deseja remover o pet '{pet.nome}'? (s/n): ")
        if confirm.lower() == 's':
            services.delete(petid)
            print("Pet removido com sucesso.")
        else:
            print("Remoção cancelada.")
    
    def listar_pets(self):
        print('Listando todos os pets')
        pets = services.get_all_pets()
        for pet in pets: # type: ignore
            print(pet)