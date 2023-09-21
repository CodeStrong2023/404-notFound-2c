#Ejercicio Tipo Set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))

print('Marte' in planetas)

planetas.add('Tierra')
print(planetas)

planetas.remove ('Venus')
print(planetas)
planetas.discard('Júpiter')
print(planetas)

planetas.clear()
print(planetas)