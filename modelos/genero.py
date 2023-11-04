import json


class Genero:

    def __init__(self,id,nombre):
        self.id = id
        self.nombre= nombre

    def establecerNombre(self,nombre):
        self.nombre=nombre

    def obtenerId(self):
        return self.id
    
    def obtenerNombre(self):
        return self.nombre

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre()
        }
