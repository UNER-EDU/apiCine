import json
import biblioteca

class Pelicula:

    def __init__(self,id,nombre,genero,director,actores,anio):
        self.__id = id
        self.__nombre= nombre
        self.__genero = genero
        self.__director = director
        self.__actores=actores
        self.__anio=anio
    
    def obtenerId(self):
        return self.__id

    def obtenerDiretor(self):
        return self.__id
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerDirctor(self):
        return self.__genero
    
    def obtenerDiretor(self):
        return self.__director
    
    def obtenerDiretor(self):
        return self.__actores

    def obtenerAnio(self):
        return self.__anio

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })


    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            # "genero": self.obtenerGenero().obtenerNombre(),
             "genero": self.obtenerGenero(),
            # "director": self.obtenerDirector().obtenerNombre(),
            "director": self.obtenerDirector(),
            "actores": len(self.obtenerActores()),
            "anio": self.__anio
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "director": self.obtenerDirector().obtenerNombre(),
            "actores": self.__mapearActores(),
            "anio": self.__anio
        }
    
    def __mapearActores(self):
        actores = self.obtenerActores()
        actoresMapa = map(lambda a: a.obtenerNombre(), actores)
        return list(actoresMapa)