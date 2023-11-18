# librerias
import os
import json

# modelos
from modelos.artista import Artista
from modelos.actor import Actor
from modelos.director import Director
from modelos.genero import Genero
from modelos.pelicula import Pelicula


class Biblioteca:
    # Ruta de archivo Luis
    #__archivoDeDatos = "H:\\UNTDF UNER\\Programacion 2\\Trabajo Practico Final\\biblioteca.json"
    #__archivoDeDatos en ruta pc Cristian
    __archivoDeDatos = "C:\\code\\Api_cine_Uner\\apiCine\\biblioteca.json"

    #colocar la ruta absoluta de su archivo biblioteca.json 
    #__archivoDeDatos = "**************\\biblioteca.json"
    
    __actores = []
    __directores = []
    __generos = []
    __peliculas = []


    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)
      
    def obtenerActores(orden=None, reverso=False):
        actores=Biblioteca.__actores
        if isinstance(orden, str):
            if orden == 'nombre':
                actores=sorted(actores,key=lambda a:a.obtenerNombre(), reverse=reverso)
            elif orden == 'colegas':
                actores=sorted(actores,key=lambda a:a.obtenerColegas(),reverse=reverso)
            elif orden == 'peliculas':
               actores=sorted(actores,key=lambda a:a.obtenerPeliculas(),reverse=reverso)
        return actores

    def obtenerDirectores(orden=None, reverso=False):
        directores=Biblioteca.__directores
        if isinstance(orden, str):
            if orden == 'nombre':
                directores=sorted(directores,key=lambda a:a.obtenerNombre(),reverse=reverso)
            elif orden == 'peliculas':
              directores=sorted(directores,key=lambda a:a.obtenerPeliculas(),reverse=reverso)
        return directores

    def obtenerPeliculas(orden=None, reverso=False):
        peliculas=Biblioteca.__peliculas
        if isinstance(orden, str):
            if orden == 'nombre':
              peliculas=sorted(peliculas,key=lambda a:a.obtenerNombre(),reverse=reverso)
            elif orden == 'director':
                peliculas = sorted(peliculas, key=lambda a: a.obtenerDirector().obtenerId(), reverse=reverso)
            elif orden == 'actores':
                peliculas = sorted(peliculas, key=lambda a: len(a.obtenerActores()), reverse=reverso)
            elif orden == 'anio':
                peliculas=sorted(peliculas,key=lambda a:a.obtenerAnio(),reverse=reverso)
        return peliculas
    
    def obtenerGeneros(orden=None, reverso=False):
        generos=Biblioteca.__generos
        if isinstance(orden, str):
            if orden == 'nombre':
               generos=sorted(generos,key=lambda a:a.obtenerNombre(),reverse=reverso)
        return generos

    def buscarActor(id):
        actorEncontrado=None
        for actor in Biblioteca.__actores:
            if actor.obtenerId()== id:
                actorEncontrado=actor                
        return actorEncontrado


    def buscarDirector(id):
        directorEncontrado=None
        for director in Biblioteca.__directores:
            if director.obtenerId()== id:
                directorEncontrado=director
        return directorEncontrado

    def buscarGenero(id):
        generoEncontrado = None
        for genero in Biblioteca.__generos:
            if genero.obtenerId()== id:
               generoEncontrado=genero
        return generoEncontrado

    def buscarPelicula(id):
        peliculaEncontrada = None
        for pelicula in Biblioteca.__peliculas:
            if pelicula.obtenerId()== id:
                peliculaEncontrada=pelicula
        return peliculaEncontrada
        

    #Metodo que debe cargar el json    
    def __parsearArchivoDeDatos():
        archivo=open(Biblioteca.__archivoDeDatos,"r")
        datos=json.load(archivo)
        archivo.close()
        return datos

    #metodo que debe cargar las listas declaradas    
    def __convertirJsonAListas(lista):
        #Obtengo el listado de peliculas
        Biblioteca.__peliculas=[]
        for pelicula in lista["peliculas"]:
             Biblioteca.__peliculas.append(Pelicula(**pelicula))

        #Obtengo el listado de actores
        Biblioteca.__actores=[]
        for actores in lista["actores"]:
            Biblioteca.__actores.append(Actor(**actores))

        #Obtengo el listado de directores
        Biblioteca.__directores=[]
        for director in lista["directores"]:
            Biblioteca.__directores.append(Director(**director))

        #Obtengo el listado de generos
        Biblioteca.__generos=[]
        for genero in lista["generos"]:
            Biblioteca.__generos.append(Genero(**genero))