class Aritmetica:
    """
    El nombre de este tipo de comentarios es: DocString
    esto es documentación de la clase python
    Vamos a hacer en esta clase algunas operaciones: suma, resta, multiplicación y más.
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Método para sumar.
    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        return self.num1 / self.num2


aritmetica1 = Aritmetica(7, 9) # Pasamos los argumentos.
print(f"La suma de los números es: {aritmetica1.sumar()}")
print(f"La resta de los números es: {aritmetica1.restar()}")
print(f"La multiplicación de los números es: {aritmetica1.multiplicar()}")
print(f"La división de los números es: {aritmetica1.dividir():.2f}")
