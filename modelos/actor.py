import json
import biblioteca 
from modelos.artista import *

class Actor(Artista):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": len(self.obtenerPeliculas()),
            # "colegas": len(self.obtenerColegas())
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
    
    #punto b
    def obtenerPeliculas(self):
        peliculas = []
        for pelicula in biblioteca.Biblioteca.obtenerPeliculas():
            if self == biblioteca.Biblioteca.obtenerActores():
                peliculas.append(pelicula)
        return peliculas

    #punto c
    def obtenerColegas(self):
        colegas = []
        for pelicula in self.obtenerPeliculas():
                for actor in pelicula.obtenerActores():
                    if actor!= self and actor not in colegas:
                        colegas.append(actor)
        return colegas
        
    #punto d
    def __eq__(self, otro):
        return self.__id == otro.obtenerId()