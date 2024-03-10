/*
Ejercicio 6: Utilizando dos matrices de tamaño 5x9 y 9x5, cargar la primera
y transponerla en la segunda.
 */
package ejerciciosde2docuatrimvacaciones;

import java.util.Scanner;

public class ejercs8 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] matrix1 = new int[5][9];
        int[][] matrix2 = new int[9][5];

        System.out.println("Introduce los elementos de la matriz de tamaño 5x9:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                matrix1[i][j] = scanner.nextInt();
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                matrix2[j][i] = matrix1[i][j];
            }
        }

        System.out.println("La matriz transpuesta es:");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }
    }
}
