/*
Ejercicio 12: Leer por teclado una tabla de 10 elementos numéricos enteros
y una posición (entre O y 9). Eliminar el elemento situado en la posición
dada sin dejar huecos.
 */
package ejerciciosde2docuatrimvacaciones;

import java.util.Scanner;

public class ejer4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tabla = new int[10];

        System.out.println("Ingrese 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Elemento " + i + ": ");
            tabla[i] = scanner.nextInt();
        }

        System.out.print("Ingrese la posición (entre 0 y 9) a eliminar: ");
        int posicion = scanner.nextInt();

        if (posicion < 0 || posicion >= 10) {
            System.out.println("Posición inválida. Debe estar entre 0 y 9.");
        } else {

            for (int i = posicion; i < 9; i++) {
                tabla[i] = tabla[i + 1];
            }
            tabla[9] = 0;

            System.out.println("Tabla después de eliminar el elemento en la posición " + posicion + ":");
            for (int i = 0; i < 10; i++) {
                System.out.print(tabla[i] + " ");
            }
        }
    }
}
