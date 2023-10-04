# Comenzamos con fucnciones
# mi_funcion() # No se puede llamar antes de difinir una funcion
# Definimos una funcion
def mi_funcion(): # Para identificar a una funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la Tecnicatura")
mi_funcion()# Estamos llamando a la funcion
mi_funcion() # Podemos llamar la funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking

def show(name, lastName):
    print(name+" "+lastName)
person =  ["Guillermo", "Giannone"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ["Ariel", "Betancud"] # Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(** person3)

numbers = [1, 2, 3, 4, 5]# Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

# Liste comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # Esto regresa una nueva lista
print(alongP)

bootleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]
Arg = [b for b in bootleC if b["country"]=="Arg"]
print(Arg)
print(bootleC)

# Paso de argumentos (funciones)
def mi_funcion2(name, lastname):
    print("Saludos a todos los que ven a traves del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastname}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a+b
#resultado = sumar(78,22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55,45)}")

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar2(22,66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")

def listarTerminos(**terminos): # Los mas utilizado es **Kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # Kwargs significa: key word argument
        print(f"{llave} : {valor}")
listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE= "Integrated Develoment Enviroment", PK = "Primary Key")
listarTerminos(Nombre = "Lionel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Tito","Pedro","Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
# desplegarNombres(10) # No es un objeto iterable
desplegarNombres((10,11)) # Para poder recorrer numero tuvimos que convertirlos en tupla, en un solo elemento no olvidar la coma
desplegarNombres([22,55]) # Tambien lo podemos convertir en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # caso base
        return 1
    else:
        return numero * factorial(numero - 1) # Caso Recursivo
numeroFactorial = int(input("Digite un numero para calcular el factorial: "))
resultado = factorial(numeroFactorial)
print(f"El factorial del numero {numeroFactorial} es: {resultado}")
