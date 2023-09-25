package clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1= new Persona(); //llamamos al constructor
        persona1.nombre="ariel";
        persona1.apellido="Betancud";
        persona1.obtenerInformacion(); //el valor hexadecimal comienza con 0x
        
        Persona persona2= new Persona();
        System.out.println("persona2: "+persona2);
        System.out.println("persona1: "+persona1);
        persona2.obtenerInformacion();
        persona2.nombre="osvaldo";
        persona2.apellido="giordanini";
        persona2.obtenerInformacion();
    }
}
