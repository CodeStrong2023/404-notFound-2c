"""
#print(ejercicios de la clase)
#ejercicio 1 : escriba un programa donde tenga una lista y que a continuacion eliminar
#los elementos repetidos, por ultimo mostrar la lista
#creamos una lista
lista=[1,2,3,"ariel",7,7,3,"alberto",1,"ariel","alberto"]
#conjunto=set(lista)#convertimos la lista a un conjunto de tipo set
#lista=list(conjunto)#convertimos el conjunto a una lista
lista=list(set(lista))
print(lista)

print("ejercicio 2") #operaciones de conjuntos con listas
#escriba un programa que tenga 7 listas y que a continuacion
#cree las siguientes listas (en las que no deben haber repeticion)
#1 lista de palabras que aparecen en las listas
#2 lista de palabras que aparecen en la primera lista , pero no en la segunda
#3 lista de palabras que aparecen en la segunda lista, pero no en la segunda
#4 lista de palabras que aparecen en ambas listas


lista1=[1,2,3,4,5,4,3,2,2,1,5]
lista2=[4,5,6,7,8,4,5,6,7,7,8]

#eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1=set(lista1)
conjunto2=set(lista2)

union=list(conjunto1|conjunto2) #unimos los dos conjuntos
solo1=list(conjunto1-conjunto2) #solo muestra el conjunto1
solo2=list(conjunto2-conjunto1) #solo muestra el conjunto2
interseccion=list(conjunto1 & conjunto2) #mostramos ambas listas

print(f"lista de palabras que aparecen en las listas: {union}")
print(f"lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}")
print(f"lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"lista de palabras que aparecen en ambas listas: {interseccion}")



#print(ejercicio 3) agregar personajes a una lista
#escribir un programa donde cree una lista con los siguientes personajes del señor de los anillos
#nombre: aragon
#clase: guerrero
#raza: dunadan del norte

#nombre: gandalf
#clase : mago
#raza: istar

#nombre: legolas
#clase: arquero
#raza: elfo sindar

personajes=[] #creamos una lista vacia
#creamos diccionarios
P1={"nombre":"aragon","clase":"guerrero","raza":"dúnadan del norte"}
personajes.append(P1)#agregamos a la lista un personaje

P2={"nombre":"gandalf","clase":"mago","raza":"istar"}
personajes.append(P2)

P3={"nombre":"legolas","clase":"arquero","raza":"elfo sindar"}
personajes.append(P3)

print(personajes) #tarea : agregar por lo menos otros 3 personajes

P4={"nombre":"aragon","clase":"guardian del anillo","raza":"elfo"}
personajes.append(P4)#agregamos a la lista un personaje

P5={"nombre":"frodo","clase":"portador del anillo","raza":"elfo"}
personajes.append(P5)

P6={"nombre":"sauron","clase":"creador del anillo","raza":"maiar"}
personajes.append(P6)

print("ejercicio matematica")
import math #importamos la clase math para hacer uso de la funcion sqrt
#dada la siguiente tupla
tupla=(13,1,8,3,2,5,8) #definimos la tupla
#crear una lista que solo incluya los numeros menores a 5
#e imprima por consola [1,3,7]
lista=[] #definimos fila lista
#filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento<5:
        lista.append(elemento)
print(lista)


#ejercicio de matematicas
#para sacar la raiz cuadrada de un numero positivo

numero=int(input("digite un numero positivo: "))
while numero<0:
    print("error -> deberia ser un numero positivo")
    numero=int(input("digite un numero positivo: "))

print(f"\nsu raiz es: {math.sqrt(numero):.2f}")


seleccionArgentina={
    10:{"nombre":"Lionel Messi","edad":35,"altura":1.70,"precio":"50 millones", "posicion":"extremo derecho"},
    11:{"nombre":"Angel Di Maria","edad":34,"altura":1.80,"precio":"12 millones","posicion":"extremo derecho"},
    24:{"nombre":"paulo dybala","edad":28,"altura":1.77,"precio":"35 millones","posicion":"media punta"},
    19:{"nombre":"Nicolas Otamendi","edad":34,"altura":1.83,"precio":"3.5 millones","posicion":"defensa central"},
    1:{"nombre":"Franco Armani", "edad":35,"altura":1.89,"precio":"3.5 millones","posicion":"portero"},

    27:{"nombre":"Julian Alvarez","edad":23,"altura":1.70,"precio":"18 millones", "posicion":"delantero"},
    7:{"nombre":"Lautaro Martinez","edad":29,"altura":1.80,"precio":"37 millones","posicion":"centrocampista"},
    22:{"nombre":"Lautaro Martinez","edad":26,"altura":1.74,"precio":"35 millones","posicion":"delantero"},
    17:{"nombre":"Alejandro Dario Gomez","edad":35,"altura":1.67,"precio":"3.5 millones","posicion":"centrocampista"},
    

}

#seguimos mostrando como recorrer un diccionario  con el ciclo for
for llave,valor in seleccionArgentina.items():
    #print(f"{i} -> {seleccionArgentina[i]}")
    print(llave,valor)




#ejercicio 1: llenar una lista: llenar una lista con los numeros del 1 al 50, luego mostra
#la lista con el bucle for, los elementos deben mostrarse de la siguiente forma: 
#1-2-3-4-5...50

#lista=[]
#i=1
#while i<=50:
#    lista.append(i)
#    i+=1

lista=list(range(1,51)) #algoritmos eficaz
for i in lista:
    print(i,end="-")



#ejercicio2: modificar los numeros de una lista, llenar una lista con los numeros del 1 al 10, 
#luego modificar los elementos de la lista multiplicandolos por un valor ingresando por el usuario
lista=list(range(1,11))
print("lista original: ")
for i in lista:
    print(i,end="-")
    
valor=int(input("\ndigite un valor a multiplicar: "))
#multiplicamos todos los elementos de la lista
for indice,i in enumerate(lista):
    lista[indice]*=valor

print(f"lista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i,end="-")

"""

print("ejercicio 3")
#insertar elementos y ordenacion

lista=[]
salir=False
while not salir:
    numero=int(input("digite un numero: "))
    if numero==0:
        salir =True
    else:
        lista.append(numero)
lista.sort() #la lista esta ordenada con esta funcion
print(f"\nLista Ordenada: \n{lista}")