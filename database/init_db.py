from database.connection import get_connection 

def create_tables():
    commands = [
        """
        DO $$ BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'servicetype') THEN
                CREATE TYPE ServiceType AS ENUM ('Consultas Veterinárias', 'Banho e Tosa');
            END IF;
        END $$;
        """,
        """
        CREATE TABLE IF NOT EXISTS Cliente(
            ClienteID SERIAL PRIMARY KEY,
            CPF CHAR(11) UNIQUE NOT NULL,
            Nome VARCHAR(100) NOT NULL,
            Telefone VARCHAR(20) NOT NULL,
            Endereco VARCHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Pet(
            PetID SERIAL PRIMARY KEY,
            Nome VARCHAR(100) NOT NULL,
            Idade INT NOT NULL,
            DataNascimento DATE NOT NULL,
            Raca VARCHAR(100),
            Especie VARCHAR(100),
            ClienteCPF CHAR(11),
            FOREIGN KEY (ClienteCPF) REFERENCES Cliente(CPF) ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Funcionario(
            FuncionarioID SERIAL PRIMARY KEY, 
            Especialidade VARCHAR(100) NOT NULL,
            Nome VARCHAR(100) NOT NULL,
            Salario DECIMAL(10, 2) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Atendimento(
            AtendimentoID SERIAL PRIMARY KEY,
            DataAtendimento DATE NOT NULL,
            Horario TIME NOT NULL,
            Servico ServiceType NOT NULL,
            PetID INT NOT NULL,
            ProfissionalID INT NOT NULL,
            ValorCobrado DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (PetID) REFERENCES Pet(PetID), 
            FOREIGN KEY (ProfissionalID) REFERENCES Funcionario(FuncionarioID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Consulta(
            ConsultaID SERIAL PRIMARY KEY,
            Motivo VARCHAR(100),
            Medicamentos VARCHAR(100),
            DataRetorno DATE,
            FOREIGN KEY (ConsultaID) REFERENCES Atendimento(AtendimentoID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Venda(
            VendaID SERIAL PRIMARY KEY,
            TotalVenda DECIMAL(10, 2) NOT NULL,
            ClienteID INT NOT NULL,
            AtendenteID INT NOT NULL,
            FOREIGN KEY (ClienteID) REFERENCES Cliente(ClienteID),
            FOREIGN KEY (AtendenteID) REFERENCES Funcionario(FuncionarioID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Produto(
            ProdutoID SERIAL PRIMARY KEY,
            Nome VARCHAR(100) NOT NULL,
            PrecoUnidade DECIMAL(10, 2) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS VendaProduto_Item (
            VendaID INT,
            ProdutoID INT,
            Quantidade INT NOT NULL,
            PRIMARY KEY (VendaID, ProdutoID),
            FOREIGN KEY (VendaID) REFERENCES Venda(VendaID),
            FOREIGN KEY (ProdutoID) REFERENCES Produto(ProdutoID)
        );
        """
    ]

    try:
        conn = get_connection()
        cur = conn.cursor()

        for i, comando in enumerate(commands, start=1):
            try:
                cur.execute(comando)
                print(f"Table {i} sucessfully created.")
            except Exception as e:
                print(f"Error on creating table {i} : {e}")

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Erro geral na conexão ou execução: {e}")

if __name__ == "__main__":
    create_tables()