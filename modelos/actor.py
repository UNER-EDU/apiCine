import json
import biblioteca 
from modelos.artista import *

class Actor(Artista):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    #mi metodo obtener Pelicula
    def obtenerPeliculas(self):
        peliculas = biblioteca.Biblioteca.obtenerPeliculas()  # Obtener todas las películas de la biblioteca
        peliculas_actor = []

        # Iterar sobre las películas para encontrar las que tienen al director actual como director
        for pelicula in peliculas:
            if pelicula.obtenerDirector() == self:
                peliculas_actor.append(pelicula)

        return peliculas_actor
       
           
    
    #mi metodo obtener Colega
    def obtenerColegas(self):
       
        pass

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
    
#c. La consulta obtenerColegas debe seguir la misma impronta que el punto 
#anterior para intentar encontrar aquellos actores que han trabajado en la 
#misma película con el actor en cuestión



    
#d. Se debe sobrecargar el operador de igualdad para que compare el 
#atributo id de cada objeto de tipo Actor.
        

