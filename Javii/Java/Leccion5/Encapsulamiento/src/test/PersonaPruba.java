
package test;

import dominio.Persona;

public class PersonaPruba {
	public static void main(String[] args) {
		Persona persona1 = new Persona("Osvaldo", 57.000, false);
		System.out.println("persona1 = " + persona1);
		//Modificar a travez de los metodos
		persona1.setNombre("Juan Ignacio");
		//System.out.println("Nombre es: "+persona1.nombre);// error
		System.out.println("persona1 su nombre es: "+persona1.getNombre());
		System.out.println("persona1 con su nombre modificado es: "+persona1.getNombre());
		System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
		System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
		
		System.out.println("persona1: "+persona1.toString());
		
	}
}
