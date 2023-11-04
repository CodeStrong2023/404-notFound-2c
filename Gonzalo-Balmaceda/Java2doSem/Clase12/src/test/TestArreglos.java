package test;

public class TestArreglos {
    public static void main(String[] args) {
        int edades[] = new int [3]; // Lado izq. Declaramos la variable / Lado derc. Instanciamos un objeto tipo object

        edades[0] = 17;
        System.out.println("edades[0] = " + edades[0]);

        edades[1] = 18;
        System.out.println("edades[1] = " + edades[1]);

        edades[2] = 19;
        System.out.println("edades[2] = " + edades[2]);

        //edades[3] = 7; // Fuera de rango (error en tiempo de ejecución).

        for (int i = 0; i < edades.length; i++) {
            System.out.println("Edades y sus elementos " + i + " = " + edades[i]);
        }
    }
}
