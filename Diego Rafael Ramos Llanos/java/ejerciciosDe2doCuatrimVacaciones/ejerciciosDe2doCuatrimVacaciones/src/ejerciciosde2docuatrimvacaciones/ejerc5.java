/*
Ejercicio 13: Leer 10 enteros en una tabla. Guardar en otra tabla los
elementos pares de la primera, y a continuación los elementos impares.
 */
package ejerciciosde2docuatrimvacaciones;

import java.util.Scanner;

public class ejerc5 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = 10;

        int[] tablaOriginal = new int[n];
        int[] tablaPares;
        int[] tablaImpares;

        System.out.println("Ingresa " + n + " enteros:");
        for (int i = 0; i < n; i++) {
            tablaOriginal[i] = scanner.nextInt();
        }

        int numPares = 0;
        int numImpares = 0;
        for (int i = 0; i < n; i++) {
            if (tablaOriginal[i] % 2 == 0) {
                numPares++;
            } else {
                numImpares++;
            }
        }

        tablaPares = new int[numPares];
        tablaImpares = new int[numImpares];

        int indicePares = 0;
        int indiceImpares = 0;
        for (int i = 0; i < n; i++) {
            if (tablaOriginal[i] % 2 == 0) {
                tablaPares[indicePares] = tablaOriginal[i];
                indicePares++;
            } else {
                tablaImpares[indiceImpares] = tablaOriginal[i];
                indiceImpares++;
            }
        }

        System.out.println("Elementos pares:");
        for (int i = 0; i < numPares; i++) {
            System.out.print(tablaPares[i] + " ");
        }
        System.out.println();

        System.out.println("Elementos impares:");
        for (int i = 0; i < numImpares; i++) {
            System.out.print(tablaImpares[i] + " ");
        }
    }
}
