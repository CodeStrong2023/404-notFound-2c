package test;

import dominio.Persona;

public class PruebaPersona2 {
    public static void main(String[] args) {
        Persona persona2 = new Persona("Gonzalo", 70.000, false);

        System.out.println("El nombre de la persona2 es = " + persona2.getNombre());
        System.out.println("El sueldo de la persona2 es = " + persona2.getSueldo());
        System.out.println("persona2 para obetener el booleano = " + persona2.isEliminado());

        // persona2 modificado.
        persona2.setNombre("Nicolas");
        persona2.setSueldo(85.000);
        persona2.setEliminado(true);

        System.out.println("El nombre de persona2 modificado es = " + persona2.getNombre());
        System.out.println("El sueldo de persona2 modificado es = " + persona2.getSueldo());
        System.out.println("El boolean de persona2 modificado es = " + persona2.isEliminado());
    }
}
