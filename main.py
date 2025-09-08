from app.models.paciente import Paciente
def main():
    print("Sistema de Gestão de Consultas - Clínica Vida & Saúde")
    
    paciente_teste = Paciente(1, "Maria Silva", "123.456.789-00", "01/01/2000", "(11)99999-9999")
    print(f"Paciente: {paciente_teste.nome} - CPF: {paciente_teste.cpf}")

if __name__ == "__main__":
    main()