import json
import biblioteca
from modelos.actor import *

class Pelicula:
    #Metodo constructor
    def __init__(self,id,nombre,genero,director,actores,anio):
        self.__id = id
        self.__nombre= nombre
        self.__genero = genero
        self.__director = director
        self.__actores=actores
        self.__anio=anio
    
    #Comandos
    def establecerNombre(self,nombre):
        self.__nombre = nombre

    def establecerGenero(self,genero):
        self.__genero=genero

    def establecerDirector(self,director):
        self.__director=director
    
    def establecerActores(self,actores):
        self.__actores=actores

    def establecerAnio(self,anio):
        self.__anio=anio

    #Consultas
    def obtenerNombre(self):
        return self.__nombre

    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    def obtenerGenero(self):
        return biblioteca.Biblioteca.buscarGenero(self.__genero)

    def obtenerDirector(self):
        return biblioteca.Biblioteca.buscarDirector(self.__director)

    """
    def obtenerActores(self):
        actores_totales = biblioteca.Biblioteca.obtenerActores()
        actores_pelicula = []

        # Recorrer los IDs de actores en la película
        for actor_id in [a["id"] for a in self.__actores]:
            # Buscar el objeto Actor correspondiente en la lista total
            actor = next((a for a in actores_totales if a.obtenerId() == actor_id), None)
            if actor:
                actores_pelicula.append(actor)
        return actores_pelicula
    """
    #menos rebuscado más legiible
    def obtenerActores(self):
        actores_totales = biblioteca.Biblioteca.obtenerActores()
        actores_pelicula = []

        # Obtener los IDs de los actores de la película
        ids_actores_pelicula = [actor["id"] for actor in self.__actores]

        # Buscar los objetos Actor correspondientes en la lista total
        for actor_total in actores_totales:
            if actor_total.obtenerId() in ids_actores_pelicula:
                actores_pelicula.append(actor_total)

        return actores_pelicula


    
    def obtenerAnio(self):
        return self.__anio

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

      
    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "director": self.obtenerDirector().obtenerNombre(),
            "actores": [actor.obtenerNombre() for actor in self.obtenerActores()],
            "cantidad de actores": len(self.obtenerActores()),
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
    
    #sobrecargando
    def __eq__(self, otro):
        return self.__id == otro.obtenerId()
