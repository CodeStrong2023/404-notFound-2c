/*
 Uso de la palabra Final
 Esta palabra tiene diferentes significados dependiendo donde
 se aplique:
    variables: Evita cambiar el valor que almacena la variable.
    métodos: Evita que se módifique la definición o el comportamiento
             de un método desde una subclase (hija).
    clases: Evita que se creen clases hijas.
 Otras caracteristicas es que normalmente, cuando trabajamos con variables
 se combina con el modificador de acceso estático para convertir una
 variable a una constante, es decir que no se puede modificar su valor.
por ejemplo la calse math
*/
package test;

import domain2.Persona;

public class TestFinal {
        public static void main(String[] args) {
        final int miDni = 432422;
        System.out.println("miDni = " + miDni);

        //miDni = 7654321; No se puede modificar.
        //Persona.CONSTANTE_AQUI = 5; // No se modifica.
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);


        final Persona persona1 = new Persona();
        //persona1 = new Persona(); 
        persona1.setNombre("rafael");
        System.out.println("persona1 = " + persona1.getNombre());

        persona1.setNombre("Liliana"); // Sí se puede modificar.
        System.out.println("persona1 = " + persona1.getNombre());
    }
}
