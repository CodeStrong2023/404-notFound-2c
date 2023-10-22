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
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 1234567;
        System.out.println("miDni = " + miDni);

        //miDni = 7654321; No se puede modificar.
        //Persona.CONSTANTE_AQUI = 5; // No se puede modificar.
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);


        final Persona persona1 = new Persona();
        //persona1 = new Persona(); // No se puede asignar una nueva referencia.
        persona1.setNombre("Gonzalo Balmaceda");
        System.out.println("persona1 = " + persona1.getNombre());

        persona1.setNombre("Nicolas"); // Sí se puede modificar.
        System.out.println("persona1 = " + persona1.getNombre());
    }
}
