class Produto:
    def __init__(self, produto_id, nome, preco_unidade):
        self.produto_id = produto_id
        self.nome = nome
        self.preco_unidade = preco_unidade

    def __repr__(self):
        return (f"Produto ID={self.produto_id}, Nome='{self.nome}', Preço Unidade={self.preco_unidade}")