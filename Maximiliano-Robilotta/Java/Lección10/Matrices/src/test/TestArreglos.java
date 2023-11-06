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
        
        for(int i = 0; i < edades.length; i++){ // lenght: longitud del arreglo.
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }
            
    }

}
