#Lista = Ariel , Liliana, Natalia, Osvaldo

nombres = ["Naty", "Osvaldo", "Lily","Ariel"]
print(nombres)
print(nombres[0:2]) #Solo muestra el indice 0, 1 pero no el indice 2
#Ir al inicio de la lista al indice (sin incluirlo)
print(nombres[  :3]) #Indices a mostrar 0,1,2
#desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
#Iterar una lista
for nombre in nombres: #Nombre es singular la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

