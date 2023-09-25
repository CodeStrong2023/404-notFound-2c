frase1 = input("Ingrese una frase: ")
frase2 = " "
for i in frase1:
    if (i != " "):
        frase2 += i

frase1 = frase2
print(f"Frase final: {frase1}")
print(f"Cantidad de caracteres en la frase {len(frase1)}")