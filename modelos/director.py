import json
import biblioteca 
from modelos.artista import Artista

class Director(Artista):

    def __init__(self,id,nombre):
        super().__init__(id,nombre)
    
    def __repr__(self):
        return json.dumps(self.convertirAJSON())
    
    def obtenerPeliculas(self):
        peliculas = biblioteca.Biblioteca.obtenerPeliculas()  # Obtener todas las películas de la biblioteca
        peliculas_director = []

        # Iterar sobre las películas para encontrar las que tienen al director actual como director
        for pelicula in peliculas:
            if pelicula.obtenerDirector() == self:
                peliculas_director.append(pelicula)

        return peliculas_director

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": len(self.obtenerGeneros()),
            "peliculas": len(self.obtenerPeliculas()),
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": self._mapearPeliculas(),
        }
    
        #punto b
    def obtenerPeliculas(self):
        peliculas = []
        for pelicula in biblioteca.Biblioteca.obtenerPeliculas():
            if self == biblioteca.Biblioteca.obtenerDirectores():
                peliculas.append(pelicula)
        return peliculas

    #punto d
    def __eq__(self, otro):
        return self.__id == otro.obtenerId()