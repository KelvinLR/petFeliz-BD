from database.super_services import SuperServices
from database.models.produtoModel import Produto


execute = SuperServices().execute_query
select = SuperServices().select

class ProdutoService:
    def get_all(self):
        rows = select(query="SELECT * FROM Produto;", fetch='all')

        return rows
    
    def get_by_id(self, produto_id: int):
        query = "SELECT produtoid, especialidade, nome, salario FROM Funcionario WHERE funcionarioid = %s;"
        row = select(query=query, params=(produto_id,),fetch='one')
        
        if row:
            return Produto(
                produto_id=row[0],
                nome=row[1],
                preco_unidade=row[2],
            )
        return None

    def add(self, produto: Produto):
        query = """
            INSERT INTO Produto (nome, precounidade)
            VALUES (%s, %s)
            RETURNING funcionarioid;
        """
        params = (produto.nome, produto.preco_unidade, produto.produto_id)
        produto.produto_id = execute(query=query, params=params, insert=True)

        return produto

    def delete(self, produtoid):
        query = "DELETE FROM Produto WHERE produtoid = %s;"
        execute(query=query, params=(produtoid,))

    def update(self, produto: Produto):
        query = """
            UPDATE Produto
            SET nome = %s, precounidade = %s
            WHERE produtoid = %s
        """
        params = (produto.nome, produto.preco_unidade, produto.produto_id)
        
        execute(query=query, params=params)