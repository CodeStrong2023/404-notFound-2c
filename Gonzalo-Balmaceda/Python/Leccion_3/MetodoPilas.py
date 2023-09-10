# Pila usando listas
pila = [1, 2, 3]

# En pilas se trabaja siempre con el último elemento.
# Agregar elementos a la pila por el final.
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final.
elementoQuitado = pila.pop()
print(f"Quitamos el elemento {elementoQuitado}")
print(f"Ahora la pila queda así {pila}")