class Persona: # creamos una clase
    #pass #no se procesa nada mas (no tiene contenido)
    def __init__(self,nombre,apellido,dni,edad,*args,**kwargs):#se lo llama metodo init dunder
        self.nombre=nombre
        self.apellido=apellido
        self._dni=dni #este atributo esta encapsulado de una manera sugerida
        self.edad=edad
        self.args=args
        self.kwargs=kwargs
    def mostrar_detalle(self): #self es igual a this
        print(f"Persona: {self.nombre},{self.apellido},{self._dni},{self.edad} direccion: {self.args}, los datos importantes son: {self.kwargs}")

persona1=Persona("ariel","betancud",32456987,40) #necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

persona2=Persona("osvaldo","giordanini",11111111,45)
print(f"el objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}")

persona1.nombre="liliana"
persona1.apellido="buccella"
persona1.edad=40
print(f"el objeto de la clase persona:{persona1.nombre},{persona1.apellido} su edad es: {persona2.edad}")
#los atributos son : caracteristicas
#los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() #la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()
#persona.mostrar_detalle(persona1) debemos pasarle una referencia para el self o dara error
persona1.telefono="33333333333344444"
print(persona1.telefono)#hemos creado un atributo de un objeto
print(f"este es el telefono de {persona1.nombre}{persona1.telefono}")

#print(persona2.telefono) #el objeto persona2 no tiene este atributo, da error
persona3=Persona("Rogelio","Romero",22222222,22,"telefono","222222","calle lopez",823,"manzana",77,"casa",18,Altura=1.83,Peso=105,CFavorito="Azul",Auto="citroen",modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar en python, esto dice que lo desconocemos


