import json
import biblioteca 
from modelos.artista import Artista

class Director(Artista):

    def __init__(self,id,nombre):
        super().__init__(id,nombre)
    
    def __repr__(self):
        return json.dumps(self.convertirAJSON())
    
    # def obtenerPeliculas(self):
    #     peliculas = biblioteca.Biblioteca.obtenerPeliculas()  # Obtener todas las películas de la biblioteca
    #     peliculas_director = []

    #     # Iterar sobre las películas para encontrar las que tienen al director actual como director
    #     for pelicula in peliculas:
    #         if pelicula.obtenerDirector() == self:
    #             peliculas_director.append(pelicula)

    #     return peliculas_director

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
            # Obtener todas las películas de la biblioteca
            peliculas = biblioteca.Biblioteca.obtenerPeliculas()
            # Crear una lista para las películas en las que participa el actor
            peliculas_dirigidas = []
            # Recorrer todas las películas
            for pelicula in peliculas:
                 peliculas_dirigidas.append(pelicula)
            # Devolver la lista de películas en las que participa el actor
            return peliculas_dirigidas



    
    """
    def obtenerPeliculas(self):
        peliculas = []
        for pelicula in biblioteca.Biblioteca.obtenerPeliculas():
            if self == biblioteca.Biblioteca.obtenerDirectores():
                peliculas.append(pelicula)
        return peliculas
      """
    



    def __eq__(self, otro):
        return isinstance(otro, Director) and self.obtenerNombre().strip().lower() == otro.obtenerNombre().strip().lower()
