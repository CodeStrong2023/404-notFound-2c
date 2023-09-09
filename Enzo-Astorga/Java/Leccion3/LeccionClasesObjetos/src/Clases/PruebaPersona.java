package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); // Llamamos al constructor, método especial dónde reserva memoria para poder crear el objeto.
        // new : palabra reservada, puntero que da acceso a espacio de memoria.
        persona1.nombre = "Enzo"; // El valor hexadecimal normalmente comienza con 0x.
        persona1.apellido = "Astorga";
        persona1.obtenerInformacion(); // Llamamos al método, muestra la información de los valores de los atributos en la clase.
        
        // Accedimos al objeto "persona1", convertido como objeto por el constructor "Persona()"
        // El constructor "Persona()" va hacia la clase Persona, una vez hecho eso
        // A través del objeto "persona1" y con el operador de punto buscamos los atributos nombre y apellido y le asignamos valores
        // Luego con el mismo objeto obtuvimos la información a través del método "obtenerInformación()" que 
        // recibe los valores y los imprime.
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Juan";
        persona2.apellido = "López";
        persona2.obtenerInformacion();
    }
    
}
