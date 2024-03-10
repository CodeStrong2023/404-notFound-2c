/*Ejercicio 5: Leer por teclado dos tablas de 10 números
enteros y mezclarlas en una tercera de la forma: el la de
A, ei la de B, ei 2a de A, ei 2a de B, etc.*/
package ejerciciosde2docuatrimvacaciones;

import java.util.Scanner;

public class ejerc2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] arrayA = new int[10];
        int[] arrayB = new int[10];
        int[] arrayC = new int[20]; 

        System.out.println("Ingrese 10 números enteros para el arreglo A:");
        for (int i = 0; i < 10; i++) {
            arrayA[i] = scanner.nextInt();
        }

        System.out.println("Ingrese 10 números enteros para el arreglo B:");
        for (int i = 0; i < 10; i++) {
            arrayB[i] = scanner.nextInt();
        }
        for (int i = 0; i < 10; i++) {
            arrayC[2 * i] = arrayA[i]; 
            arrayC[2 * i + 1] = arrayB[i]; 
        }

        System.out.println("Arreglo combinado C:");
        for (int i = 0; i < 20; i++) {
            System.out.print(arrayC[i] + " ");
        }
    }
}
