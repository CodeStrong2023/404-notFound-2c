nombres = ['Nagy', 'Osvaldo', 'Lily', 'Ariel']
"""print(nombres)
print( nombres[0])
print( nombres[1])
print( nombres[3])
print( nombres [-1])
print( nombres[-2])"""

print (nombres)
print (nombres [0:2])

print (nombres [0:3])

print (nombres [1: ])
nombres[2]="liliana"
nombres[0]="natalia"
print(nombres)

for nombre in nombres:
    print(nombre)
else: print("se acabaron los nombres")

print(len(nombres))
nombres.append("marcelo")
print(nombres)

nombres.insert(1,"alverto")
print(nombres)
nombres.insert(3,"debora")
print(nombres)

nombres.remove("alverto")
print(nombres)

nombres.pop()
print(nombres)

del nombres[2]
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombre)
#definimos un tupla
cocina=("cuchara","cuchillo","tenedor")
print(len(cocina))

print(cocina[0])
print(cocina[0:1])

verdura=("papa",)

for cocinar in cocina:
    print(cocinar, end=" ")

cocinalit=list(cocina)
cocinalit[0]="plato"
cocina=tuple(cocinalit)
print("\n",cocina)


