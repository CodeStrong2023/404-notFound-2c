package pasoporreferencia;

import paquetePersonaCopiadoParaLaClase6.Persona;

public class PasoPorReferencia {

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre= " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("el cambio que hicimos en el nombre es: " + persona1.nombre);
       // persona1 =cambiarElValor(persona1);
        //Persona persona2=null;
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
         System.out.println("El nuevo valor de objeto es : " + persona2.nombre);
    }

    public static void cambiarValor(Persona persona) { //parametro por referencia
        persona.nombre = "Maria";
        return;
    }

    public static Persona cambiarElValor(Persona persona) {
        if (persona == null) {
            System.out.println("Valor de persona invalido : null");
            return null;
        } else {
            persona.nombre = "monica";
            System.out.println("m= "+persona.nombre);
            return persona;
        }
    }
}
