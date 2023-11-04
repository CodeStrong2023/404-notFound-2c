# lista = Arie, Liliana, Natalia, Osvaldo
#Colecciones de python
nombres = ["Naty" , "Osvaldo" , "Lily" , "Ariel"]
print(nombres)
print(nombres [0])
print(nombres [1])
print(nombres [3])
print(nombres [-1])
print(nombres [-2])
print(nombres [0:2]) #solo  muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluiro)
print(nombres [ :3]) # Indices a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres [1:])
# Modificamos un valor
nombres[3] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append(7)
print(nombres)

# Insertar un eemento en un indece especifico
nombres.insert(1, "Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

# Elimnar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)

#Eliminar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
#print(nombres)# Aquí nos da error

# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedir')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])
#Ejemplo
verduras =('papa',) #una tupla auque sea un elemento necesita una coma
# De la contrario solo seria un tipo str cadena
#Recorremos los elementos de una tupla
for cocinar in cocina:#Print esta usando /n para salto de lineas
    print(cocinar, end= ' ') #usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('/n', cocina)

#del cocina # esto es para eliminar la tupla

# Tipos set
planetas = {'Marte' , 'Jupiter' , 'Venus'}
print(len(planetas)) #Usamos la funcion len = length significa largo

# Revisar si un elemento existe dentro de set
print('Marte' in planetas)

# Agregar un elemento
planetas.add('Tierra') #add es una funcion
print(planetas)

# Eliminar elementos, puede arrojar un error si el element no existe
planetas.remove('Jupiter')#Esta función ante un mal ingreso u inexistencia del elemento arroja error
print(planetas)
planetas.discard('Tierra')#Esta funcion no nos presenta ningun error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

# Eliminar set
del planetas
#print(planetas)# Al eliminar nos muestra error

# 'Maradona': 10 un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE' : 'integrated Development Environment',
    'POO' : 'Programación Orientada a Objetos',
    'SABD' : 'Sistema de Administracion de Basa de Datos'
    }
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6]
lista3 = lista1+lista2 # Concatenamos
print(lista3)

lista3.extend([7, 8, 9]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Función para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) esto daria un error por no ser el elemento parte de la lista

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

#Para poner nuestra lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos

lista = [lista3]* 2
print(lista3)

# Metodos de ordenamiento
lista3.sort() # Ordena los elementos ascendentes
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

#Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

print(4 in tupla) # Accion tipo booleana, se resp es tipo booleana
# lo que podemos usar dentro de tuplas son: index, count, len
# en tupla se puede convertir de tupla a lista y de lista a tupla

#Repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye'}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos is e numero 3 no esta en el conjunto 1

#como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #nos devuelve como respuesta booleana

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor del conjunto1 y n o del conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunta es un subconjunto dento de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))
print(conjunto2.issubset(conjunto3))

# Como saber si ambos conjuntos son disconexos, si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2))

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totalmente inmutable
#No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso diccionario
diccionarioNuevo = {'Azul', 'Blue', 'Rojo', 'Red', 'Verde', 'Green', 'Amarillo', 'Yellow'}
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia':[35, 1.67]}
print(diccionario2)

seleccionArgentina= {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo derecho' },
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millonres', 'Posicion': 'Extremo derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
    23: {'Nombre': 'Emiliano Martines', 'Edad': 31, 'Altura': 1.95, 'Precio': '28 millones', 'Posicion': 'Portero'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 29, 'Altura': 1.80, 'Precio': '40 millones', 'Posicion': 'Mediocentro'}
}
print(seleccionArgentina)
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print('Tenemos cargados en el diccionario la cantidad de jugadores:', end= '')
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #Quita el ultimo elemento y lo guarda en la variable
print(f'sacamos el elemeno: {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

#colas con listas
#Estructura de datos de tipo fifo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente:{seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el ciente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
