"""
ejercicio 10: no repetir caracteres
hacer un programa que pida una cadena por
teclado, luego meter los caracteres en una
lista sin repetir caracteres


cadena=input("ingrese cadena: ")
lista=[]
for i in cadena:
    if i not in lista: #si el caracter aun no esta en la lista
        lista.append(i) #lo agregamos a la lista
print(f"\nLista de caracteres sin repetir ninguno: \n{lista}")

"""

"""
ejercicio 11: agenda telefonica
hacer un programa que simule una agenda de contactos.
crear un diccionario donde la clave sea el nombre del usuario
y el valor sea el telefono, el programa tendra el siguiente
menu de opciones
|||1)nuevo contacto
   2)borrar contacto
   3)ver contactos existentes
   4)salir


agenda={}
while True:
    print("\tMENU")
    print("1 nuevo contacto")
    print("2 borrar contacto")
    print("3 ver contactos existentes")
    print("4 salir")
    opcion=int(input("digite una opcion de menu:"))

    if opcion==1:
        nombre=input("ingrese el nombre del contacto: ")
        telefono=input("ingrese el telefono:" )
        if nombre not in agenda:
            agenda[nombre]=telefono
            print("contacto agregado")
        else:
            print("este nombre ya eciste")
    elif opcion==2:
        nombre=input("cual es el nombre del contacto: ")
        if nombre in agenda:
            del(agenda[nombre])
            print("se ha eliminado el contacto")
        else:
            print("este contacto no existe")
    elif opcion==3:
        print("agenda de contactos")
        for clave , valor in agenda.items():
            print(f"nombre: {clave},telefono: {valor}")
    elif opcion==4:
            print("gracias , nos vemos")
            break;
"""
"""
#comenzamos con funciones
#mi_funcion() #no se puede llamar antes de definir a una funcion
#definimos una funcion
def mi_funcion():#para identificar a la funcion utilizamos parentesis
    print("saludos a todos los alumnos de la tecnicatura")

mi_funcion() #estamos llamando a la funcion
mi_funcion() #se puede llamar a una funcion N cantidad de veces

#desempaquetado de listas o list unpacking
def show(name,lastName):
    print(name+" "+lastName)

person=["ariel","betancud"]
show(person[0],person[1])#pasamos uno por uno los datos de la lista a la funcion
show(*person)#esto es lo mismo que lo anterior pero le pasamos todo junto

person2=("osvaldo","giordanini")#desempaquetamos a travez de una tupla
show(*person2)
person3={"lastName":"Lucero","name":"Natalia"}
show(**person3)

numbers=[1,2,3,4,5]
for n in numbers:
    print(n)
    if n==3:
        break;#esta es la unica manera para que no se ejecute el else
else:
    print("esto se termina")


#list comprehension . lista de comprension
names=["paolo","rodrigo","lupe","pepe"]
alongP=[p for p in names if p[0]=="p"]#esto regresa una nueva lista
print(alongP)

bottleC=[{"name":"quilmes","country":"Arg"},
            {"name":"corona","country":"Mx"},
            {"name":"Stella Artois","country":"Belgium"},
            
            ]

Arg=[b for b in bottleC if b["country"]=="Arg"]
print(Arg)
print(bottleC)

#paso por argumentos(funciones)
def mi_funcion2(name,lastName):
    print("saludos a todos los alumnos de la tecnicatura")
    print(f"nombre: {name}, apellido: {lastName}")

mi_funcion2("jorge","lucero")
mi_funcion2("ariel","betancud")
mi_funcion2("Analia","Pedrosa")

#la palabra return en funciones
#creamos una funcion para sumar

def sumar(a,b):
    return a+b

resultado=sumar(78,22)
print(f"el resultado de la suma es: {resultado}")
print(f"el resultado de la suma es: {sumar(78,22)}")

def sumar2(a=0,b=0):#le damos un valor por default
    return a+b

resultado=sumar2()
print(f"el resultado de la suma es: {resultado}")
print(f"el resultado de la suma: {sumar2(22,66)}")

#argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
    
listarNombres("lucas","jose","claudia","rosa","maria")
listarNombres("marcos","daniel","romina","pepe","marcela"m"carlos)
"""
#ej 1: crear una funcion para sunar los valores prohibidos de tipo 
#numericos utilizando argumentos variables *args como parametro
#de la funcion y agregar como resultado la suma de todos los valores
#pasados como argumentos
#definimos una funcion
def sumar_valor(*args): #recibimos una cantidad de parametros indefinidos
    pass

#llamamos a la funcion
print(sumar_valor(3,5,9,2))
