/*
Ejercicio 14: Leer dos series de 10 enteros, que estarán ordenados crecientemente.
Copiar (fusionar) las dos tablas en una tercera, de forma que sigan ordenados.
 */
package ejerciciosde2docuatrimvacaciones;

import java.util.Arrays;
import java.util.Scanner;

public class ejerc6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array1 = new int[10];
        int[] array2 = new int[10];
        int[] array3 = new int[20];

        System.out.println("Introduce 10 números enteros ordenados crecientemente para la primera serie:");
        for (int i = 0; i < 10; i++) {
            array1[i] = scanner.nextInt();
        }

        System.out.println("Introduce 10 números enteros ordenados crecientemente para la segunda serie:");
        for (int i = 0; i < 10; i++) {
            array2[i] = scanner.nextInt();
        }

        System.arraycopy(array1, 0, array3, 0, 10);
        System.arraycopy(array2, 0, array3, 10, 10);
        Arrays.sort(array3);

        System.out.println("La tercera serie fusionada y ordenada es: " + Arrays.toString(array3));
    }
}
