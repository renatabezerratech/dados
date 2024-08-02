from sqlalchemy import create_engine, text

# String de conexão para o banco de dados MySQL
engine = create_engine(
    'mysql+pymysql://root:rbf#250904@localhost/db_testeConexao'
)

def inserir_dados():
    # Solicita os dados ao usuário
    nome = input("Digite o Nome: ")
    idade = input("Digite a Idade (número inteiro): ")

    # Verifique se os valores inseridos estão corretos
    print(f"Nome: {nome}, Idade: {idade}")
    
    # Monta a consulta SQL para inserir os dados
    consulta = text("""
        INSERT INTO exemplo (nome, idade)
        VALUES (:nome, :idade)
    """)
    
     # Executa a consulta SQL
    with engine.connect() as connection:
        try:
            connection.execute(consulta, { "nome": nome, "idade": idade})
            connection.commit()
            print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")


# Chama a função para inserir os dados
if __name__ == "__main__":
    inserir_dados()


    # MySQL:
    # USE db_testeconexao;
    # SELECT * FROM exemplo;
