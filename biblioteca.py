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

    __archivoDeDatos = "C:\\co\\Programacion 2\\Trabajo Practico Final\\biblioteca.json"
    #__archivoDeDatos ="c:\\code\\apiCine\\biblioteca.json"
    #__archivoDeDatos en ruta pc Cristian
    __actores = []
    __directores = []
    __generos = []
    __peliculas = []

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)
        

    def obtenerActores(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass # completar
            elif orden == 'colegas':
                pass # completar
            elif orden == 'peliculas':
                pass # completar
        pass # completar

    def obtenerDirectores(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass # completar
            elif orden == 'peliculas':
                pass # completar
        pass # completar

    def obtenerPeliculas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass # completar
            elif orden == 'director':
                pass # completar
            elif orden == 'actores':
                pass # completar
            elif orden == 'anio':
                pass # completar
        pass # completar

    def obtenerColegas(orden=None, reverso=False):
        pass #

    def obtenerGeneros(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass # completar
        pass # completar

    def buscarActor(id):
        for actor in Biblioteca.__actores:
            if actor.obtenerId()== id:
                return actor
        return None


    def buscarDirector(id):
        pass # completar

    def buscarGenero(id):
        pass # completar

    def buscarPelicula(id):
        pass # completar

    #Metodo que debe cargar el json    
    def __parsearArchivoDeDatos():
        archivo=open(Biblioteca.__archivoDeDatos,"r")
        datos=json.load(archivo)
        archivo.close()
        return datos

    #metodo que debe cargar las listas declaradas    
    def __convertirJsonAListas(lista):
        Biblioteca.__peliculas=[]
        for pelicula in lista["peliculas"]:
             Biblioteca.__peliculas.append(Pelicula(**pelicula))
             print(Biblioteca.__peliculas[0])