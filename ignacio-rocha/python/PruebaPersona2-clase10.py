from clase10 import *
print("creacion de objetos: ".center(50,"-"))
if __name__=="__main__":
    persona1=Persona2("lionel","messi",35)
    persona1.mostrar_detalle()

    print(__name__)
print("eliminacion de objetos".center(30,"-"))
del persona1