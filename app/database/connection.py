import sqlite3 #Driver de banco de dados embutido no Python
from pathlib import Path #Path a achar o arquivo schema.sql de forma

DB_PATH = "clinica.db" #Nome do arquivo do banco de dados

SCHEMA_FILE = Path(__file__).with_name("schema.sql")
#Aponta o caminho app/database/schema.sql

def get_connection(): #Abre uma conexão SQLite e liga as chave estrangeira
    conn = sqlite3.connect(DB_PATH) #Abre ou cria o banco de dados
    conn.execute ("PAGMA foreign_keys = ON") #Liga a integridade referencial (FKs) no SQLite
    return conn #Devolve a conexão para os repostitórios/services

def init_db(): #Executa o arquivo schema.sql (cria tabelas/inices e faz do usuario adm, se necessário)
    "Usamos a palvra 'with' para garantir que o arquivo será fechado após o uso"
    with get_connection() as conn: #Abre o arquivo de chema(UTF-8) para aceitr
        with open(SCHEMA_FILE, "r", enconding = "utf-8") as f:
            sql = f.read()
            conn.executescript(sql)