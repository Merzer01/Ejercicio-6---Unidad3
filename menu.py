class Menu(object):
    def showmenu(self):
        print('''
--------MENU PRINCIPAL--------
1 - 
2 -
3 -
4 -
5 -
6 -
        ''')
        cond = False
        while not cond:
            op = int(input("Ingrese numero de opcion: "))
            if op in [1,2,3,4,5,6]:
                cond=True
        return cond