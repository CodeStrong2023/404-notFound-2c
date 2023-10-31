"""

##ejercicio 10: no repetir caracteres
##hacer un programa que pida una cadena por
##teclado, luego meter los caracteres en una
##lista sin repetir caracteres


cadena=input("ingrese cadena: ")
lista=[]
for i in cadena:
    if i not in lista: #si el caracter aun no esta en la lista
        lista.append(i) #lo agregamos a la lista
print(f"\nLista de caracteres sin repetir ninguno: \n{lista}")


##ejercicio 11: agenda telefonica
##hacer un programa que simule una agenda de contactos.
##crear un diccionario donde la clave sea el nombre del usuario
##y el valor sea el telefono, el programa tendra el siguiente
##menu de opciones
##|||1)nuevo contacto
##   2)borrar contacto
##   3)ver contactos existentes
##   4)salir



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
listarNombres("marcos","daniel","romina","pepe","marcela","carlos")

def listarTerminos(**terminos):#lo mas utilizado es **kwargs para recibir los argumentos
    for llave,valor in terminos.items():#kwargs significa : key word argument
        print(f'{llave}:{valor}')

listarTerminos() #no recibe nada, nada se va a mostrar
listarTerminos(IDE="Integrated Development  Enviroment",PK='Primary Key')
listarTerminos(nombre="Leonel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2=["Tito","Pedro","Carlos"]
desplegarNombres(nombres2)
desplegarNombres("carla")
#el valor de tipo int no es iterable
desplegarNombres((10,11))#la convertimos a una tupla,en un solo elemento no olvidar la coma
desplegarNombres([22,55])# la convertimos en una lista

#funciones recursivas
def factorial(numero):
    if numero==1: #caso base
        return 1
    else:
        return numero *factorial(numero-1) #caso recursivo
numero=int(input("ingrese nro: "))
resultado=factorial(numero) #lo hacemos en codigo duro
print(f"el resultado es {resultado}")



"""
#ej 1: crear una funcion para sunar los valores prohibidos de tipo
#numericos utilizando argumentos variables *args como parametro
#de la funcion y agregar como resultado la suma de todos los valores
#pasados como argumentos
#definimos una funcion
def sumar_valor(*args): #recibimos una cantidad de parametros indefinidos
    resultado=0
    #iteramos cada elemento
    for valor in args:
        resultado+=valor
    return resultado

#llamamos a la funcion
print(sumar_valor(3,5,9,2))

#ejercicio 2: funcion con * args para multiplicar
#crear una funcion para multiplicar los valores
#recibidos de tipo numerico, utilizando argumentos
#variables *args como parametro de la funcion y
#regresar como resultado la multiplicacion
#de todos los valores pasados como argumentos

#definimos la funcion para multiplicar
def multiplicar_valores(*args):#el mas utilizado es *args
    resultado=1#el cero no nos ayuda a multiplicar
    for numero in args:
        resultado*=numero
    return resultado

#llamamos a la funcion
print(multiplicar_valores(3,5,15,3))#le pasamos los argumentos

##ejercicio 3:funcion recursiva
##imprimir numeros de 5 a 1 de manera descendente
##usando funciones recursivas puede ser cualquier valor positivo,
##por ejemplo, si pasamos el valor de 5, debe imprimir:
##    5
##    4
##    3
##    2
##    1
##en caso de ser 3 debe mostrar:
##    3
##    2
##    1
##si se ingresan nros negativos no imprime nada

nro=int(input("ingrese nro: "))
def imprimir_numeros_recursivos(numero):
    if numero>=1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero==0:
        return
    elif numero<=0:
        print("valor incorrecto")
imprimir_numeros_recursivos(nro)

##ejercicio 4: calculadora de impuestos
##crear una funcion para calcular el total de un pago
##incluyendo un impuesto aplicado (IVA)
##formula: pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
##proporcione el pago sin impuesto:1000
##proporcione el monto del impuesto: 21%
##pago con impuesto: xxxxx
##
##creamos la funcion que calcula el total del pago incluyendo el impuesto

def calcular_total_pago(pago_sin_impuesto,impuesto):
    pago_total=pago_sin_impuesto+pago_sin_impuesto*(impuesto/100)
    return pago_total

#ejecutamos la funcion
pago_sin_impuesto=float(input("ingrese el pago sin impuestos: "))
impuesto=float(input("digite el monto del impuesto a aplicar: "))
pago_con_impuesto=calcular_total_pago(pago_sin_impuesto,impuesto)
print(f"el pago con impuesto es: {pago_con_impuesto}")
"""
##ejercicio 5: convertidor de temperatura
##realizar dos funciones para convertir de grados celsius
##a fahrenheit y viceversa. investigar las formulas
##
##funcion que convierte de celsius a fahrenheit

def celsius_farenheit(celsius):
    return celsius*9/5+32 #la precedencia:multiplicacion,division,suma

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32)*5/9 # respetar la precedencia usando parentesis

celsius=float(input("digite el valor de celsius: "))
resultado=celsius_farenheit(celsius)
print(f"{celsius} C a F ->{resultado:.2f}")

fahrenheit=float(input("ingrese el valor de fahrenheit: "))
resultado=fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F a C {resultado:.2f}")