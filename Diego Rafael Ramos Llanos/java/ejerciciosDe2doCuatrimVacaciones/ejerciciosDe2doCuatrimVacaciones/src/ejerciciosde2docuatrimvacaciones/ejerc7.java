/*
Ejercicio 15: Leer 10 enteros ordenados crecientemente. Leer N y buscarlo en la
tabla. Se debe mostrar la posición en que se encuentra. Si no está, indicarlo
con un mensaje.
 */
package ejerciciosde2docuatrimvacaciones;

import java.util.Scanner;

public class ejerc7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[10];
        System.out.println("Introduce 10 números enteros ordenados crecientemente:");
        for (int i = 0; i < 10; i++) {
            array[i] = scanner.nextInt();
        }
        System.out.println("Introduce el número N a buscar:");
        int N = scanner.nextInt();
        int pos = -1;
        for (int i = 0; i < 10; i++) {
            if (array[i] == N) {
                pos = i;
                break;
            }
        }
        if (pos == -1) {
            System.out.println("El número N no se encuentra en la tabla.");
        } else {
            System.out.println("El número N se encuentra en la posición: " + (pos + 1));
        }
    }
}
