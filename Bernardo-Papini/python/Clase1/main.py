# lista = Ariela, Liliana, Natalia, Osvaldo.

nombres = ['Naty', 'Osvaldo' , 'Lili', 'Ariel']
print(nombres)
print(nombres[0:2]) # Solo muestra el índice 0, 1 pero no el índice 2

# Ir del inicio de la lista al índice (sin incluirlo):
print(nombres[ :3]) # Mostré los índice 0,1 y 2

# Desde el índice indicado hasta el final:
print(nombres[1: ])

# Modificamos un valor:
nombres[0] =  'Natalia'
nombres[2] = 'Liliana'
print(nombres)

# Iterar nuestra lista
for nombre in nombres: # nombre es singular, lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista.')

# Preguntamos cuántos elementos tiene:
print(len(nombres)) # Es una función que nos regresa la cantidad de elementos que contiene una lista.
# Le pasamos como parámetro a la lista

# Agregamos un elemento:
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un índice específico:
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Débora')
print(nombres)

#  Eliminamos un elemento:
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento:
nombres.pop()
print(nombres)

# Eliminamos un índice específico:
del nombres[2] #del (delete) significa eliminar
print(nombres)

# Eliminar, borrar o limpiar todos los elementos:
nombres.clear()
print(nombres)

# Eliminar la lista:
del nombres
# print(nombres) # Aquí muestra el error

# Definimos una tupla:
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no paréntesis:
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a rango:
print(cocina[0:2])
# Ejemplo:
verduras = ('papa') # Sin la coma pasa a ser un elemento cadena de tipo string y deja de ser una tupla
print(verduras)

# Recorremos los elementos de la tupla:
for cocinar in cocina: # Print está usando la diagonal \n para saltar líneas
    print(cocinar, end=' ') # Usamos end= para eliminar saltos de línea

# Esta conversión de tupla a lista y de lista a tupla no es buena práctica de la programación:
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple (cocinaLista)
print("\n", cocina)

# En TUPLAS no se pueden utilizar las funciones append, insert y remove
# Si el programa necesitará modificarse usaremos una lista y si no queremos modificaciones usaremos una tupla

# Eliminamos la tupla:
del cocina
# print(cocina) # Muestra el error

# SET es una colección que no tiene un orden y no permite almacenar elementos duplicados o repetidos, no se puede modificar

# pero si se puede agregar o eliminar.
# No mantiene ningún índice, el orden es aleatorio.
# Set puede servir para evitar la repetición de datos en una base de datos. Ej(Documentos, patentes, etc.)

# Tipo Set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # Usamos la función len = lenght significa largo

# Revisar si un elemento existe dentro de Set
print('Marte' in planetas)

# Revisar si un elemento no existe dentro de Set
print('Júpiter' not in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una función para añadir en conjuntos
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') # Esta función ante un mal ingreso o inexistencia de elemento da error
print(planetas)

planetas.discard('Tierra') # Esta función discard no nos presenta ningún error
print(planetas)

# Limpiar Set o conjunto
planetas.clear()
print(planetas)

# Eliminar Set o conjunto
del planetas
# print(planetas)

# 'Maradona': 10 Un diccionario está compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}

# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando las llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una función para acceder al valor
    print(valor) # Muestra los valores sin las llaves

# Comprobar la existencia de algún elemento
print('IDE' in diccionario) # devuelve un booleano

# Comprobar la inexistencia de algún elemento
print('IDE' not in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario
# print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Esta es una función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función para saber en que índice está cada elemento
# print(lista3.index(0)) # Esto da error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner nuestra lista al revés
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento, en python es una función
lista3.sort() # Ordena siempre de manera ascendente
print(lista3)

# Para ordenar de manera descendente
lista3.sort(reverse=True)
print(lista3)

# Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Preguntamos si está o no el elemento, responde en booleano
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla