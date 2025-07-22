from database.services.produtoService import ProdutoService
from database.models.produtoModel import Produto

services = ProdutoService()

class ProdutoController:
    def produto_create(self):
        print("Digite as informações solicitadas")
        nome = input("Nome: ")
        preco_unidade = input("Preço Unidade: ")
        id = None

        new_produto = Produto(produto_id=id, nome=nome, preco_unidade=preco_unidade)
        services.add(new_produto)

    def update_produto(self):
        print("Digite as informações solicitadas")
        produto_id = input("Digite o ID do produto que deseja atualizar: ")
        produto = services.get_by_id(produto_id)

        if produto is None:
            print("Produto não encontrado.")
            return

        print(f"Produto atual: {produto}")
        print("Deixe em branco para manter o valor atual.")

        nome = input(f"Novo nome ({produto.nome}): ") or produto.nome
        preco_unidade = input(f"Novo preço unidade ({produto.preco_unidade}): ") or produto.preco_unidade

        produto.preco_unidade = preco_unidade
        produto.nome = nome

        services.update(produto)

    def buscar_produto(self):
        print("\nDigite as informações solicitadas")
        produto_id = input("Digite o ID do produto: ")
        produto = services.get_by_id(produto_id)
        if produto:
            print("Produto encontrado:")
            print(produto)
        else:
            print("Produto não encontrado.")
    
    def remover_produto(self):
        print("\nDigite as informações solicitadas")
        produto_id = input("Digite o ID do produto: ")
        produto = services.get_by_id(produto_id)

        if produto is None:
            print("Produto não encontrado.")
            return
            
        confirm = input(f"Tem certeza que deseja remover o produto '{produto.nome}'? (s/n): ")
        if confirm.lower() == 's':
            services.delete(produto_id)
            print("Produto removido com sucesso.")
        else:
            print("Remoção cancelada.")

    def listar_produtos(self):
        print('Listando todos os produtos')
        produtos = services.get_all()
        for produto in produtos: # type: ignore
            print(produto)