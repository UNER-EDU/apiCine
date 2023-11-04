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

    __archivoDeDatos = "biblioteca.json"
    __actores = []
    __directores = []
    __generos = []
    __peliculas = []

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    # def inicializar(self):

    # # Parsear el archivo JSON
    #     datos = self.__parsearArchivoDatos() 

    #     # Convertir el JSON a las listas
    #     self.__convertirJsonAListas(datos)

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

    def obtenerGeneros(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == 'nombre':
                pass # completar
        pass # completar

    def buscarActor(id):
        pass # completar

    def buscarDirector(id):
        pass # completar

    def buscarGenero(id):
        pass # completar

    def buscarPelicula(id):
        pass # completar

    def __parsearArchivoDeDatos():
        pass # completar

    def __convertirJsonAListas(lista):
        pass # completar
