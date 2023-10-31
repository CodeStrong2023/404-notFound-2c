#clase 2
#tipo set
planetas={"marte","jupiter","venus"}
print(planetas)
print(len(planetas)) #usamos la funcion len =length significa largo
#revisar si un elemento existe dentro de set
print("jupiter" in planetas)

#agregar un elemento
planetas.add("tierra")#add es una funcion
print(planetas)

#eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("jupiter")#esta funcion ante un mal ingreso o inexistencia del elemento da error
print(planetas)
planetas.discard("tierra")#esta funcion no nos presenta ningun error
print(planetas)
#limpiar set
planetas.clear()
print(planetas)

#eliminar set
del planetas

#print(planetas) #al eliminar nos muestra fun error

#"maradona":10 un diccionario esta compuesto por dos  elementos
#una llave y un valor
#dict(key,value)
diccionario={
    "ide":"integrated development enviroment",
    "poo":"programacion orientada a objetos",
    "sabd":"sistema de administracion de base de datos"

}
print(len(diccionario))
print(diccionario)

#acceder a un diccionario con la llave(key)
print(diccionario["ide"])

#otra forma de recuperar un elemento
print(diccionario.get("poo"))
print(diccionario.get("sabd"))

#modificamos elementos
diccionario["ide"]="entorno de desarrollo integrado"
print(diccionario)

#como recorrer los elementos
for termino in diccionario:#recorremos mostrando solo las llaves
    print(termino)

#necesitamos una funcion para recorrer un diccionario
for termino,valor in diccionario.items():
    print(termino,valor)

#necesitamos una funcion para acceder un diccionario
#for termino,valor in diccionario.keys():#estamos usando una funcion
#    print(termino) #muestra solo las llaves

for valor in diccionario.values():#usamos una funcion para acceder el valor
    print(valor)

#comprobar la existencia de algun elemento
print ("ide" in diccionario)#devuelve un booleano

#agregar un elemento
diccionario["PK"]="primary key"
print(diccionario)

#eliminar un elemento
diccionario.pop("sabd")
print(diccionario)

#vaciar un diccionario
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario #diccionario se borro

#concatenamos listas
lista1=[1,2,3]
lista2=[4,5,6]
lista3=lista1+lista2
print(lista3)
lista3.extend([7,8,9]) #funcion para agregar varios elementos
print(lista3)
print(lista3.index(5)) #funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0))

#como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))#cuenta cuantos valores iguales hay dentro de una lista

#para poner al reves una lista
lista3.reverse()
print(lista3)

#para que una lista se multiplique repitiendo sus elementos
lista3=lista3*2
print(lista3)

#metodos de ordenamiento
lista3.sort() #ordena los elementos ascedentemente
print(lista3)
lista3.sort(reverse=True) #ordena descendentemente
print(lista3)

tupla=(4,"hola",6.78,[1,2,78],4,"hola") #puede tener distintos tipos de datos dentro

print(tupla)
print(4 in tupla)#accion booleana su respuesta es de tipo booleana

#lo que podemos usar dentro de tuplas son: index,count,len
#en tuplas se puede convertir de tupla a lista y de lista a tupla








