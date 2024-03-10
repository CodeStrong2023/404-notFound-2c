/*
Ejercicio 11: Leer 5 elementos numéricos que se introducirán ordenados de forma
creciente. Éstos los guardaremos en una tabla de tamaño 10. Leer un número N,
e insertarlo en eI lugar adecuado para que la tabla continúe ordenada.
 */
package ejerciciosde2docuatrimvacaciones;
import java.util.Scanner;

public class ejer3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] array = new int[10];

        System.out.println("Ingrese 5 números enteros ordenados de forma creciente:");
        for (int i = 0; i < 5; i++) {
            array[i] = scanner.nextInt();
        }

        System.out.println("Ingrese un número entero N:");
        int num = scanner.nextInt();

        int sitio_num = 0;
        while (sitio_num < 10 && array[sitio_num] < num) {
            sitio_num++;
        }

        for (int j = 9; j >= sitio_num; j--) {
            array[j] = array[j - 1];
        }
        array[sitio_num] = num;

        System.out.println("Arreglo resultante:");
        for (int i = 0; i < 10; i++) {
            System.out.print(array[i] + " ");
        }
    }
}


