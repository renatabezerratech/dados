
# instalei: pip install pymysql


from sqlalchemy import create_engine  # conectando ao BD
from sqlalchemy import MetaData, Table, Column, Integer, String


# String de conexão para o banco de dados MySQL
engine = create_engine(
    'mysql+pymysql://root:**********@localhost/db_testeConexao'
)

# Criação de uma tabela
metadata = MetaData()

exemplo = Table(
    'exemplo', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50)),
    Column('idade', Integer)
)

# Conectar ao banco de dados e criar a tabela
with engine.connect() as connection:
    metadata.create_all(engine)

print("Tabela criada com sucesso!")



# Para testar a conexão, você pode tentar se conectar e listar as tabelas do banco de dados
#with engine.connect() as connection:
#    result = connection.execute("SHOW TABLES;")
#    for row in result:
#        print(row)
