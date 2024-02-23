/*
Ejercicio 4: Leer 10 números enteros, guardarlos en un
arreglo. Debemos mostrarlos en eI siguiente orden: eI primero.
el último, eI segundo, el penúltimo, eI tercero, etc.
 */
package ejerciciosde2docuatrimvacaciones;

import java.util.Scanner;

public class ejerc1 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        int num = 0;

        Scanner scanner = new Scanner(System.in);
        while (num < 10) {
            System.out.print("Ingresa un número entero: ");
            numeros[num] = scanner.nextInt();
            num++;
        }
        System.out.println("Números en el orden especificado:");
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]);
            if (i != 4) {
                System.out.println(numeros[9 - i]);
            }
        }
        scanner.close();
    }
}
