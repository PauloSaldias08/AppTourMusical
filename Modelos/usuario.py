import json

class Usuario:
    def __init__(self, id, nombre, apellido, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**usuario) for usuario in data]