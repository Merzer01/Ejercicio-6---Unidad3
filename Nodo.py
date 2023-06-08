class Nodo:
    __dato: None
    __siguiente: None
    def __init__(self, dato, sig):
        self.__dato = dato
        self.__siguiente = sig

    def setsiguiente(self, sig):
        self.__siguiente = sig
    def getsiguiente(self):
        return self.__siguiente
    def getdato(self):
        return self.__dato