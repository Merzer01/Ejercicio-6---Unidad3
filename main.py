from objectencoder import ObjectEncoder
from classVehiculo import Vehiculo
from classNuevo import Nuevo
from classUsado import Usado
from menu import Menu
from classLista import Lista
import json
import os


def cargaVehiculo():
    print('''
Vehiculos
1 - Nuevos
2 - Usados
    ''')
    op = int(input("Ingrese opcion de vehiculo: "))
    mod = str(input("Ingrese modelo del vehiculo: "))
    puerta = int(input("Ingrese cantidad de puertas: "))
    color = str(input("Ingrese color del vehiculo: "))
    precio = int(input("Ingrese precio base del vehiculo: "))
    if op == 1: #nuevos
        print("MARCA -> TOYOTA")
        version = str(input("Ingrese version del vehiculo: "))
        xv = Nuevo(mod, puerta, color, precio, version)
    elif op == 2: #usados
        patente = str(input("Ingrese patente: "))
        marca = str(input("Ingrese marca: "))
        año = int(input("Ingrese año: "))
        km = int(input("Ingrese cantidad de kilometros: "))
        xv = Usado(mod, puerta, color, precio, patente, marca, año, km)
    return xv

if __name__ == '__main__':
    os.system('cls')
    lista = Lista()
    JsonF = ObjectEncoder()
    dicc = JsonF.LeerArchivo('vehiculos.json')
    lista = JsonF.decodificarDiccionario(dicc)
    band = False
    while not band:
        menu = Menu()
        opcion = menu.showmenu()
        if opcion == 1:
            xv = cargaVehiculo()
            pos = int(input("Ingrese la posicion en la que añadir el elemento: "))
            lista.insertarElemento(xv, pos)
        elif opcion == 2:
            xv = cargaVehiculo()
            lista.agregarElemento(xv)
        elif opcion == 3:
            pos = int(input("Ingrese la posicion en la que añadir el elemento: "))
            lista.mostrarElemento(pos)
        elif opcion == 4:
            patente = str(input("Ingrese patente: "))
            precio = lista.precio_patente(patente)
            print("Precio de venta: {}".format(precio))
        elif opcion == 5:
            economico = lista.economimo()
            if economico != None:
                print(economico.mostrar)
        elif opcion == 6:
            ''
        elif opcion == 0:
            print("Saliendo")
            band = True
        else: print("Opcion incorrecta!!!")
    os.system('pause')
    os.system('cls')
    
    
    
    '''n = (...)
    L.agregar(n)
    pos = int(input("Posicion: "))
    L.mostrar()
    economico = L.economico()
    if L.economico () != None:
        economico.mostrar()'''