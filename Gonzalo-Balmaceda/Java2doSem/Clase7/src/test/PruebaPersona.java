package test;

import dominio.Persona;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 50.000, false);

        System.out.println("persona1 su nombre es = " + persona1.getNombre());

        // Modificamos a través de los métodos.
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; // Ya no se puede utilizar al ser privado.

        //System.out.println("Nombre es = " + persona1.nombre); // Error
        System.out.println("persona1 con su nombre modificado es = " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo es = " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano = " + persona1.isEliminado());

        // Llamamos al toString.
        System.out.println("persona1 = " + persona1); // Se accede al toString automáticamente.
    }
}
