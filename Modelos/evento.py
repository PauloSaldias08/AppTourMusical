import json

class Evento:
    def __init__(self, id, nombre, genero, artista, id_ubicacion ,hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.genero = genero
        self.artista = artista
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion 
        self.imagen = imagen

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**evento) for evento in data]
    
    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_locales(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Evento.de_json(json.dumps(dato)) for dato in datos]
