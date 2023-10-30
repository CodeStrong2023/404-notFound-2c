package arreglos_ejercicio_2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
         /*
        Ejercicios 2 = Leer 5 números, guardarlos en un arreglo y mostrarlos
        en el orden inverso.
        */

        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];

        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Ingrese un número: ");
            numeros[i] = entrada.nextFloat();
        }

        // Mostramos los números ingresados en el arreglo de manera inversa.
        System.out.println("Mostramos los números ingresados de manera inversa: ");
        for (int i = numeros.length - 1; i >= 0; i--) {
            System.out.println(numeros[i]);
        }
    }
}
