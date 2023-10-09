# Comenzamos con Funciones
# mi_funcion No se puede llamar antes de definir una función
# Definimos una funciónde

def mi_funcion():  # Para identificar a la función utilizamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura!")


mi_funcion()  # Estamos llamando a la función.
mi_funcion()
mi_funcion()  # Se puede llamar a una función N cantidad de veces


# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + " " + lastName)


person = ["Ariel", "Betancud"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la función
show(*person)  # Esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ("Osvaldo", "Giordanini")  # Desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

# REPASO CICLO FOR ELSE
numbers = [1, 2, 3, 4, 5]  # Aún con la lista vacía se ejecuta el else.
for n in numbers:
    print(n)
    if n == 3:
        break  # Ésta es la única manera para que no se ejecute el else.
else:
    print("Esto se terminó.")

# List conprehension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alonP = [p for p in names if p[0] == "P"]  # Esto regresa una nueva lista.
print(alonP)  # Imprime una lista con los nombres con "P" mayúscula.

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belguim"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)


# Pason de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que nos ven a través del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")  # PARÁMETROS (VARIABLES QUE DECLAREMOS EN LA FUNCIÓN)


mi_funcion2("Jorge", "Lucero")  # ARGUMENTOS (VALOR QUE ENVIAMOS A LA FUNCIÓN Y QUE RECIBE EL PARÁMETRO)
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analía", "Pedrosa")


# La palabra Return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b  # Regresamos el resultado desde el return.


# resultado = sumar(78, 22) # Asignamos a la variable, el resultado que está enviando nuestra función.
# print(f"El resultado de la suma es: {resultado}")
print(f"El resiltado de la suma es: {sumar(55, 45)}")  # Llamamos a la función desde la función print.


# Valores por default en los parámetros de una función
def sumar2(a=0, b=0):  # Le damos un valor pot default
    return a + b


resultado = sumar2()
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar2(22, 66)}")


# Argumentos, variables en funciones
def listarNombres(*nombres):  # Normalmente se utiliza: *args
    for nombre in nombres:  # nombres: Se convierte en una tupla
        print(nombre)


listarNombres("Lucas", "José", "Claudia", "Rosa", "María")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela",
              "Carlos")  # Puede recibir cantidad de argumentos que varían uniendose a la función


# Argumentos variables para un diccionario
def listarTerminos(**terminos):  # kwargs: Llave, palabras y argumentos, el más utilizado para recibir los argumentos
    for llave, valor in terminos.items():  # kwargs: key word arument
        print(f"{llave} : {valor}")


listarTerminos()  # Nada se va a mostrar
listarTerminos(IDE="Integrated Develoment Enviroment", PK="Primaruy Key")
listarTerminos(Nombre="Lionel Messi")


# Lista de elementos con funciones (convertir)
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")  # Se muestra con cada uno de los elementos, recorriendo cada uno de ellos
# desplegarNombres(10, 11) OBJETO ENTERO NO ES ITERABLE
desplegarNombres((10,))  # Si usamos paréntesis se convierte en una tupla iterable,
# los paréntesis corresponden a las tuplas (Usar coma si o si aunque sea un solo elemento)
desplegarNombres([22, 55])  # También podemos convertirlo en una lista


# Funciones recursivas con factorial
# Una función recursiva se manda a llamar a sí misma para completar una cierta tarea
def factorial(numero):  # Caso Base
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)  # Caso Recursivo
numeroFactorial = int(input("Digite el número para calcular el factorial: "))  # Tarea que el usuario ingrese el número para calcular el factorial
resultado = factorial(numeroFactorial)  # Lo hacemos en código duro
print(f"El factorial del número {numeroFactorial} es: {resultado}")


