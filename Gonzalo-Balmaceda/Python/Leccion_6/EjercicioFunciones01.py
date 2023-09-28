def sumarValor(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(sumarValor(5, 3, 2))