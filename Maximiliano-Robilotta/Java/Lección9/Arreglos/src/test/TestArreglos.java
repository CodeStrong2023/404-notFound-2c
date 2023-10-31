/*
Arreglos:
Conjunto de elementos dónde vamos a poder agregar de diferente tipo.
No solo puede tener tipo primitivo también puede combinarse con tipos Object
en Java.
Comienzan en el índice 0, la última posición es N1 dónde N es la cantidad de 
elementos que contiene un arreglo.
 */
package test;

public class TestArreglos {
    public static void main(String[] args) {
        int edades[] = new int[3]; // Lado izq: Declaramos variable - Lado der: instanciamos un objeto de tipo arreglo(object).
        System.out.println("edades = " + edades);
        
        // Modificamos los elementos del arreglo:
        edades[0] = 17;
        System.out.println("edades 0 = " + edades[0]);
        edades[1] = 22;
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 18;
        System.out.println("edades 2 = " + edades[2]);
        
        // edades[3] = 7; // Fuera de rango, error en tiempo de ejecución.
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }
            
    }

}
