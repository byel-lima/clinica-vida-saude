from typing import List, Optional
from app.models.paciente import Paciente
from app.database.connection import get_connection #Função utilitária para abrir a conexão com o banco de dados

class PacienteRepository:
    def create(self, paciente:Paciente):
        """" INSERE UM NOVO PACIENTE E RETORNA O ID GERADO"""
        conn = get_connection()
        try:
            cur = conn.execute("""INSERT INTO paciente (nome, cpf, data_nascimento, telefone) VALUES (?, ?, ?, ?)""", 
                               (paciente.nome, paciente.cpf, paciente.data_nascimento, paciente.telefone)
            )
            conn.commit() #Salva no banco
            return cur.lastrowid #Devolve o id de novo registro
        finally:
            conn.close() #Fecha a conexão sempre
    
    def find(self, nome:str | None = None, cpf: str | None = None)-> List[Paciente]:
        """ Lista pacientes por filtro opcionais (nome, cpf) """
        con = get_connection()