import json
from pathlib import Path
from classLista import Lista
from classVehiculo import Vehiculo
from classNuevo import Nuevo
from classUsado import Usado

class ObjectEncoder(object):

    def decodificarDiccionario(self, d, lv):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                vehiculos=d['vehiculos']
                Lista=class_()
                for i in range(len(vehiculos)):
                    xVehiculo=vehiculos[i]
                    class_name=xVehiculo.pop('__class__')
                    class_=eval(class_name)
                    atributos=xVehiculo['__atributos__']
                    unVehiculo=class_(**atributos)
                    lv.agregarElemento(unVehiculo)
            print ('Se cargaron los vehiculos!')
            return Lista

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
            print ('Se guardó el archivo correctamente')

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)