class Consulta:
    def __init__(self, id, paciente_id, medico_id, data, hora, status):
        self.id = id
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.data = data
        self.hora = hora
        self.status = status  #Agendada, Canselada, Realizada 
