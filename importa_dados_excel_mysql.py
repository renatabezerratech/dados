import pandas as pd
from sqlalchemy import create_engine

# Configurações do MySQL
user = 'root'
password = 'rbf#250904'
host = 'localhost'
database = 'db_PRODUTOS'

# Criar a URL de conexão
connection_string = f'mysql+mysqldb://{user}:{password}@{host}/{database}'
engine = create_engine(connection_string)

# Ler a planilha Excel
df = pd.read_excel('Planilha_exemplo_produto.xlsx')

# Inserir dados no banco de dados
df.to_sql('tab_produtos', engine, if_exists='replace', index=False)

print("Dados importados com sucesso!")
