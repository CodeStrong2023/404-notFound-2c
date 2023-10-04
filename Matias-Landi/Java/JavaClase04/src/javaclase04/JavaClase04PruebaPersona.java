
package javaclase04;

public class JavaClase04PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Matías"; //El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Landi";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona2);
        persona2.obtenerInformacion();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
    }
}
