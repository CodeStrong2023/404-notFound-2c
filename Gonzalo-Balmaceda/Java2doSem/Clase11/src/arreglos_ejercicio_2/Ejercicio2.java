package arreglos_ejercicio_2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
           /*
        Ejercicios 2 = Leer 5 números, guardarlos en un arreglo y mostrarlos
        en el orden inverso.
        */
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int[5];

        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Ingrese un número: ");
            numeros[i] = entrada.nextInt();
        }

        // Mostramos el arreglo en el orden inverso.
        System.out.println("\nMostramos el arreglo en el orden inverso");
        for (int i = 4; i >= 0; i--) {
            System.out.println(numeros[i]);
        }
    }
}
