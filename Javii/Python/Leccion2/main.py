# Comenzamos con Funciones
#mi_funcion() #No se puede llamar antes de definir una funcion
#Definimos una funcion
def mi_funcion(): #Para identificar la funcion utilizamos parentesis
    print("Saludos a todos los estudiantes de la tecnicatura")

mi_funcion() #Estamos llamando a la funcion
mi_funcion() #Se puede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") #desempaquetamos a travez de una sola tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbrers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbrers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

#List comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de argumentos (Funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a travez del canal de youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

#La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado es la suma es: {sumar(55,45)}")

def sumar2(a:int = 0, b:int = 0): #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: #Se va a convertir en una tupla
        print(nombre)
listarNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")
listarNombres("Marcos", "Daniel", "Romina", "Pepe")

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

listarTerminos() #No recibe nada, nada va a mostrar
listarTerminos(IDE = "Integrated Develoment Enviroment", PK = "Primaruy Key")
listarTerminos(Nombre = "Leonel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 =["Tito","Pedro","Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
#desplegarNombres(10, 11)# No es un objeto iterable
desplegarNombres((10, 11)) #La covertimos a una tupla
desplegarNombres([22,55])#La convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1:# Caso base
        return 1
    else:
        return numero * factorial(numero-1)#Caso recursivo

numeroFactorial = int(input("Digite el numero para calcular el factorial: "))
resultado = factorial(numeroFactorial) #Lo hacemos en codigo duro
print(f"El factorial del numero {numeroFactorial} es: {resultado}")
