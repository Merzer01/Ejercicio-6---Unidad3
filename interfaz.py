from zope.interface import interface

class Interfaz(interface):
    def insertarElemento(self, elemento, posicion):
        pass
    def agregarElemento(self, elemento):
        pass
    def mostrarElemento(self, posicion):
        pass