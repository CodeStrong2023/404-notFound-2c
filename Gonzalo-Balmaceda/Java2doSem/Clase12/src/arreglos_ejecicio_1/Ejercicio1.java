package arreglos_ejecicio_1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        /*
        Ejercicios 1 = Leer 5 números, guardarlos en un arreglo y mostrarlos
        en el mismo orden introducidos.
        */

        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];

        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Ingrese un número: ");
            numeros[i] = entrada.nextFloat();
        }

        // Mostramos los números ingresados en el arreglo
        System.out.println("Los número ingresados en el arreglo son: ");
        for (float i : numeros) {
            System.out.println(i + " ");
        }
    }
}
