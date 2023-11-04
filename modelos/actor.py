import json
import biblioteca
from modelos.artista import Artista

class Actor(Artista):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerActor(self):
        return self

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": len(self.obtenerPeliculas()),
            "colegas": len(self.obtenerColegas())
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": self._mapearPeliculas(),
            "colegas": self.__mapearColegas()
        }
    
    def __mapearColegas(self):
        colegas = self.obtenerColegas()
        colegasMapa = map(lambda a: a.obtenerNombre(), colegas)
        return list(colegasMapa)
    
#c. La consulta obtenerColegas debe seguir la misma impronta que el punto 
#anterior para intentar encontrar aquellos actores que han trabajado en la 
#misma película con el actor en cuestión



    
#d. Se debe sobrecargar el operador de igualdad para que compare el 
#atributo id de cada objeto de tipo Actor.
        

