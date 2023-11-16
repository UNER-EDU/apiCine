import json
import biblioteca 
from modelos.artista import Artista

class Director(Artista):

    def __init__(self,id,nombre):
        super().__init__(id,nombre)
    
    def __lt__(self, otro_actor):
        return self.nombre < otro_actor.nombre
    
    def __repr__(self):
        return json.dumps(self.convertirAJSON())
    
    def obtenerPeliculas(self):
        peliculas = biblioteca.Biblioteca.obtenerPeliculas()  # Obtener todas las películas de la biblioteca
        peliculaDirector = []
        # Iterar sobre las películas para encontrar las que tienen al director actual como director
        for pelicula in peliculas:
            if pelicula.obtenerDirector() == self:
                peliculaDirector.append(pelicula)
        return peliculaDirector

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
    
    def __eq__(self, otro):
        return (isinstance(otro, Director)
                    and self.obtenerNombre() == otro.obtenerNombre())
