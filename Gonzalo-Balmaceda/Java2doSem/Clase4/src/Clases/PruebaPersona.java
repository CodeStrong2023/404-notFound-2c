package Clases;

public class PruebaPersona {
    public static void main(String[] args) {

        Persona persona1 = new Persona(); // Llamamos al constructor.

        // Accedemos a los atributos de la clase.
        persona1.nombre = "Gonzalo";
        persona1.apellido = "Balmaceda";

        // Accedemos al método.
        persona1.obtenerInformacion();

        // Creamos un segundo objeto.
        Persona persona2 = new Persona();

        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";

        persona2.obtenerInformacion();
    }
}
