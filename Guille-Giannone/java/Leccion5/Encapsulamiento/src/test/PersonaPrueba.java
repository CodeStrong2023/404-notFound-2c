
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.001,false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        System.out.println("persona1 = " + persona1);
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio";//Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre);//Error
        System.out.println("Persona1 con su nombre modificado es: "+persona1.getNombre());
        System.out.println("Persona1 el resultado para su sueldo: "+persona1.getSueldo());
        System.out.println("Persona1 para obtener el booleano es: "+persona1.isEliminado());
        
        //Tarea: Crear objeto de tipo Persona, asiganar valores de manera inicial e imprimir,
        //luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona("Guillermo",60.001,true);
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        System.out.println("persona2 el resultado de sueldo es: "+persona2.getSueldo());
        System.out.println("persona2 para obtener booleano es: "+persona2.isEliminado());
        
        persona2.setNombre("Rafael");
        persona2.setSueldo(71.001);
        persona2.setEliminado(false);
        
        System.out.println("persona2 su nombre modificado es: "+persona2.getNombre());
        System.out.println("persona2 el resultado de su sueldo modificado es: "+persona2.getSueldo());
        System.out.println("persona2 para obtener booleano modificado es: "+persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1);
    }
}
