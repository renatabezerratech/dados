
# OLTP
# BD transacional - operação
# Dados: inclusão, leitura, alteração, exclusão

import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import sqlite3

# Configurações de banco de dados
DATABASE_NAME = "transacional.db"
DATABASE_PATH = f"sqlite:///{DATABASE_NAME}"
engine = create_engine(DATABASE_PATH)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

def create_table_from_csv(csv_path):
    """Cria uma tabela com base em um arquivo CSV"""
    df = pd.read_csv(csv_path)
    table_name = os.path.splitext(os.path.basename(csv_path))[0]

    columns = [Column('id', Integer, primary_key=True, autoincrement=True)]
    for column in df.columns:
        columns.append(Column(column, String))
    
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)

    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Tabela '{table_name}' criada com sucesso.")

def query_table(table_name):
    """Consulta todos os dados de uma tabela"""
    with engine.connect() as connection:
        result = connection.execute(f"SELECT * FROM {table_name}").fetchall()
        for row in result:
            print(row)

def update_record(table_name, column_name, old_value, new_value):
    """Atualiza um registro em uma tabela"""
    try:
        with engine.connect() as connection:
            connection.execute(f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {column_name} = '{old_value}'")
            print("Registro atualizado com sucesso.")
    except IntegrityError:
        print("Erro ao atualizar o registro. Verifique as restrições de integridade.")

def delete_record(table_name, column_name, value):
    """Deleta um registro de uma tabela"""
    try:
        with engine.connect() as connection:
            connection.execute(f"DELETE FROM {table_name} WHERE {column_name} = '{value}'")
            print("Registro deletado com sucesso.")
    except IntegrityError:
        print("Erro ao deletar o registro. Verifique as restrições de integridade.")

def save_and_exit():
    """Finaliza a sessão e encerra o programa"""
    session.commit()
    session.close()
    print("Alterações salvas e programa encerrado.")
    exit()

def main():
    while True:
        print("\nMenu:")
        print("1. Carregar CSV para o banco de dados")
        print("2. Consultar dados")
        print("3. Atualizar registro")
        print("4. Deletar registro")
        print("5. Salvar e encerrar")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            csv_path = input("Digite o caminho do arquivo CSV: ")
            create_table_from_csv(csv_path)
        elif choice == '2':
            table_name = input("Digite o nome da tabela: ")
            query_table(table_name)
        elif choice == '3':
            table_name = input("Digite o nome da tabela: ")
            column_name = input("Digite o nome da coluna a ser atualizada: ")
            old_value = input("Digite o valor atual: ")
            new_value = input("Digite o novo valor: ")
            update_record(table_name, column_name, old_value, new_value)
        elif choice == '4':
            table_name = input("Digite o nome da tabela: ")
            column_name = input("Digite o nome da coluna: ")
            value = input("Digite o valor a ser deletado: ")
            delete_record(table_name, column_name, value)
        elif choice == '5':
            save_and_exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
