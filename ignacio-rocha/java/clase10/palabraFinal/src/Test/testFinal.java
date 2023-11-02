package Test;

import domain.Persona;

public class testFinal {
    public static void main(String[] args) {
        final int miDni=40855566;
        System.out.println("miDni = " + miDni);
        //miDni=40855566 no se puede modificar
        //Persona.CONSTANTE_AQUI=9; //no se modifica
        System.out.println("mi atributo constante es:"+Persona.CONSTANTE_AQUI);
        final Persona persona1=new Persona();
        //persona1=new Persona();no se puede asignar una nueva referencia
        persona1.setNombre("Ariel");
        System.out.println("persona: "+persona1.getNombre());
    }
}
