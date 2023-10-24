# Comenzamos con Funciones
# mi_funcion #No se puede llamar antes de definir una función
# Definimos una funciónde

def mi_funcion():  # Para identificar a la función utilizamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura!")
mi_funcion()  # Estamos llamando a la función.
mi_funcion()
mi_funcion()  # Se puede llamar a una función N cantidad de veces

def show(name, lastName):
    print(name + " " + lastName)
person = ["Diego", "Rafael"]
show(person[0], person[1])
show(*person)
# Desempaquetamos a traves de una tupla.
tupla = ("Osvaldo", "Giordanini")
show(*tupla)
# Desempaquetamos un diccionario.
persona3 = {"lastName": "Lucero", "name": "Natalia"}
show(**persona3)
numeros = [1, 2, 3, 4, 5]

for i in numeros:
    print(i)
    if ( i == 3):
        break
else:
    print("Esto se terminó")
nombres = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in nombres if p[0] == "P"]
print(alongP)

bottleC = [{"Name": "Quilmes", "Country": "Arg"},
           {"Name": "Corona", "Country": "Mx"},
           {"Name": "Stella Artois", "Country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["Country"] == "Arg"]

print(Arg)
print(bottleC)

def mi_funcion2(name,lastName):
    print("saludos a todos los alumnos de la tecnicatura")
    print(f"nombre: {name}, apellido: {lastName}")

mi_funcion2("jorge","lucero")
mi_funcion2("ariel","betancud")
mi_funcion2("Analia","Pedrosa")

def sumar(a,b):
    return a+b

resultado=sumar(55,45)
print(f"el resultado de la suma es: {resultado}")
print(f"el resultado de la suma es: {sumar(78,22)}")

def sumar2(a=0,b=0):#asignamos un valor por default
    return a+b

resultado=sumar2()
print(f"el resultado de la suma es: {resultado}")
print(f"el resultado de la suma: {sumar2(22,66)}")


def listarNombres(*nombres):#se combierten en una tupla
    for nombre in nombres:
        print(nombre)
listarNombres("lucas", "jose", "claudia", "rosa", "maria")
listarNombres("marcos", "daniel", "romina", "pepe", "marcela","carlos")

def listarTerminos(**terminos):
    for key, value in terminos.items():
        print(f"{key} : {value}")

listarTerminos() # Si no recibe nada, no va a mostrar nada.
listarTerminos(IDE="Integrated Develoment Enviroment", PK="Primaruy Key")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ["tito", "pedro", "carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
#desplegarNombres(10, 11) # No es un objeto iterable.
desplegarNombres((10, 11)) # La convertimos en una tupla.
desplegarNombres([22, 55]) # La convertimos en una lista.

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(5)
print(f"El facotial del número 5 es : {resultado}")