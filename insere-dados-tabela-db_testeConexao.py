from sqlalchemy import create_engine, text

# String de conexão para o banco de dados MySQL
engine = create_engine(
    'mysql+pymysql://root:rbf#250904@localhost/db_testeConexao'
)

def inserir_dados():
    # Solicita os dados ao usuário
    id = input("Digite o ID (número inteiro): ")
    nome = input("Digite o Nome: ")
    idade = input("Digite a Idade (número inteiro): ")

    # Verifique se os valores inseridos estão corretos
    print(f"ID: {id}, Nome: {nome}, Idade: {idade}")
    
    # Monta a consulta SQL para inserir os dados
    consulta = text("""
        INSERT INTO exemplo (id, nome, idade)
        VALUES (:id, :nome, :idade)
    """)
    
     # Executa a consulta SQL
    with engine.connect() as connection:
        try:
            connection.execute(consulta, {"id": int(id), "nome": nome, "idade": int(idade)})
            print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")


# Chama a função para inserir os dados
if __name__ == "__main__":
    inserir_dados()


    # MySQL:
    # USE db_testeconexao;
    # SELECT * FROM exemplo;
