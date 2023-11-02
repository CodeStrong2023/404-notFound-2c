package test;

import dominio.*;
import ContextoEstatico.domain.Persona;
public class PersonaPrueba {
    private int contador;
    public static void main(String[] args) {
        
        /*
        Persona persona1=new Persona("osvaldo",57.000,false);
        System.out.println("persona1 su nombre es:"+ persona1.getNombre());
        //modificar a traves de los metodos
        persona1.setNombre("juan ignacio");
        //persona1.nombre="juan ignacio"; //ya no se puede utilizar
        //System.out.println("nombre es: "+persona1.nombre);
        System.out.println("persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        Persona persona2=new Persona("pedro",10,true);
        System.out.println("persona2 su nombre modificado es: "+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());
        System.out.println("persona1: "+persona1);
        */
        Persona persona1=new Persona("ariel");
        System.out.println("persona1 = " + persona1);
        Persona persona2=new Persona("naty");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        //this.contador=10; //no se puede referenciar desde un contexto estatico
        PersonaPrueba personaP1=new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }
    
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    public int getContador(){
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
}















