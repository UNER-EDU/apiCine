import json
import biblioteca 
from modelos.artista import *

class Actor(Artista):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.id=id
        self.nombre=nombre

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
    
    def obtenerPeliculas(self):
        # Obtener todas las películas de la biblioteca
        peliculas = biblioteca.Biblioteca.obtenerPeliculas()
        # Crear una lista para las películas en las que participa el actor
        peliculaActuadas = []
        # Recorrer todas las películas
        for pelicula in peliculas:
            # Obtener la lista de actores de la película
            actorePelicula = pelicula.obtenerActores()
            # Verificar si el actor actual está en la lista de actores de la película
            if self in actorePelicula:
                # Agregar la película a la lista del actor
                peliculaActuadas.append(pelicula)
        # Devolver la lista de películas en las que participa el actor
        return peliculaActuadas
        
    def obtenerColegas(self):
        colegas = []
        for pelicula in self.obtenerPeliculas():
                for actor in pelicula.obtenerActores():
                    if actor!= self and actor not in colegas:
                        colegas.append(actor)
        return colegas
      
    def __eq__(self, otro):
        return isinstance(otro, Actor) and self.obtenerNombre() == otro.obtenerNombre()
