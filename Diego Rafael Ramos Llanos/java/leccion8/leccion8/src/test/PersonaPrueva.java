
package test;
import dominio.*;
public class PersonaPrueva {
    public static void main(String[] args) {
        Persona persona1=new Persona("osvaldo",57.000,false);
        System.out.println("persona1 su nombre es:"+ persona1.getNombre());
        //modificar a traves de los metodos
        persona1.setNombre("juan ignacio");
        //persona1.nombre="juan ignacio"; //ya no se puede utilizar
        //System.out.println("nombre es: "+persona1.nombre);
        System.out.println("persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        //Tarea: crear otro objeto de tipo persona , asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y luego vover a imprimir con los valores nuevos
    }
}
