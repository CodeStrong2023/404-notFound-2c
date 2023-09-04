# Lista = Ariel, Liliana, Natalia, Osvaldo
# Colecciones en Python
# Las lista son las que se conocen como arreglos o vectores
# Mostramos los nombres de adelante para atras con numero positivo y de atras para adelante con numero negativo
nombres = ["Naty","Lily","Osvaldo","Ariel"]
'''print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])'''

print(nombres[0:2]) #Solo muestra el indice 0,1. Pero no muestra el indice 2
print(nombres[ :3]) # muestra desde el inicio de la lista hasta la posicion que le indicamos
print(nombres[1: ]) # muestra desde el indice indicado hasta el final de la lista

nombres[1] = "Liliana" # Modificamos el valor del indice
nombres[0] = "Natalia"
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es en plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# preguntamos cuantos elementos tiene la lista
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento a la lista
nombres.append("Marcelo")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un indice especifico

nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

# Eliminar un elemto

nombres.remove("Alberto")
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)
# Eliminar un indice especifico
del nombres[2]
print(nombres)

#Eliminar, borrar o limpiar la lista
nombres.clear()
print(nombres)

# Eliminar la lista. Nos muestra error porque no esta definida, ya fue eliminada
del nombres
#print(nombres)

# definimos una Tupla
cocina = ("Cuchara","Cuchillo","Tenedor")
print(cocina)
print(len(cocina)) # nos dice cuantos elementos tiene

# Acceder a un elemento dentro de una Tupla, para esto utilizamos corchetes
print(cocina[0]) # nos indica el elemento de la primer posicion
print(cocina[-1]) # mostramos de mandera inversa

# Acceder a un rango
print(cocina[0:1])

# Ejemplo
verduras = ("papas",) # para que sea una tupla aunque tenga un solo elemento debe tener la coma
# de lo contrario seria una cadena de tipo str

# Recorremos los elementos de la tupla
for cocinar in cocina:
   #print(cocinar) # Print esta usando el \n para saltos de linea
    print(cocinar, end=" ") # usamos end=" " para eliminar los saltos de linea del print

# Esta es la unica forma de cambiar un elemento de una tupla, nunca se aconseja hacerlo
cocinaLista = list(cocina) # convertimos la tupla en lista
cocinaLista[0] = "Plato" # modificamos el elemento
cocina = tuple(cocinaLista) # volvemos la lista a tupla
print("\n", cocina)

#del cocina # esta es la forma de eliminar la tupla

# Tipo set
planetas = {"Marte","Jupiter","Venus"}
print(planetas)
print(len(planetas)) # Utilizamos la funcion len = lengthsignifica largo

# Revisamos si el elemento esta dentro de set
print("Marte" in planetas) # preguntamos por si # debemos escribir el elemento exactamente igual que donde fue asignado de lo contrario nos dira que es falso
print("Marte" not in planetas) # preguntamos por no

# Agregar un elemento
planetas.add("Tierra") # add es una funcion
print(planetas)

# Eliminar elementos
planetas.remove("Jupiter") # si no se escribe exactamente igual la consola nos arrojara un error
print(planetas)
planetas.discard("Tierra") # con esta funcion no nos arroja error pero tampoco elimina sino esta escrito igual
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muestra fun error

# Un diccionario esta compuesto de por dos elmentos
# "MARADONA" : 10 # UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    "IDE" : "Integrated Development Environment",
    "POO" : "Programacion Orientada a Objetos",
    "SABD" : "Sistema de Administracion de Base de Datos"
}
print(diccionario)
print(len(diccionario)) # para ver la cantidad de elementos

# Acceder a un diccionario con la llave (key)
print(diccionario ["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# Modificar elementos
diccionario ["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)
# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una funcion
    print(termino) # Muestra solo las llaves
for valor in diccionario.values(): # Usamos esta funcion para mostrar los valores
    print(valor)

# Comprobar la existencia de algun elemento
print("IDE" in diccionario) # devuelve un valor booleano

# Agregar un elemento a diccionario
diccionario ["PK"] = "Primary Key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario # Con solo eso el diccionario se borro
#print(diccionario) # larga error porque ya no existe diccionario

# Concatenar listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1 + lista2  # Concatenamos
print(lista3)

lista3.extend([7,8,9,1]) # Esta es una funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice se encuentra el valor ingresado
#print(lista3.index(0)) # esto daria error por no formar parte de la lista

# Como saber cuantos valores repetidos hay en una lista
print(lista3.count(1)) # cuenta cuantos valores iguales hay en la lista

# Para poner alreves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort() # Esta funcion ordena los elementos de forma ascendente
print(lista3)
lista3.sort(reverse=True) # Esta funcion los ordena de forma descendente
print(lista3)

# Repaso de tuplas
tupla = (4,"Hola",6.78,[6,7,8],4,"Hola")  # Puede tener diferentes tipos de datos dentro
print(tupla)
print(4 in tupla) # Accion booleana, la respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas de puede convertir de tupla a lista y de lista a tupla


