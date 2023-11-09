/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo de donde
se aplique:
      variables: Evita cambiar el valor que almacena la variable
      métodos: Evita que se modifique la definición o el comportamiento
               de un metodo
      clases: Evita que se creen clases hijas
Otra caracteristicca es que normalmente, cuando trabajamos con variables
se combina con el modificador de acceso estático para convertir una
variable en una constante, es decir que no se puede modificar su valos,
el jemplo de esto es la clase Math en la cual todos sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce
como una constante.
*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 35912813;
        System.out.println("miDni = " + miDni);
        //miDni = 34285999;//No se puede modificar
        //Persona.CONSTANTE_AQUI = 9;//No se modifica
        System.out.println("Mi atributo constante " +Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede asignar una nueva variable
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre: "+persona1.getNombre());
    }
}
