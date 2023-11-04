package matriz_ejercicio_03;

import java.util.Scanner;

public class Ejercicios03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros [][] = new int [3][3];

        // Llenamos la matriz.
        System.out.println("Llenado de la matriz: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("matriz["+i+"]["+j+"]: ");
                numeros[i][j] = entrada.nextInt();
            }
        }
        System.out.println();

        // Matriz original.
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++ ) {
                System.out.println(numeros[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();

        // Matriz transpuesta.
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++ ) {
                System.out.println(numeros[j][i]+" ");
            }
            System.out.println(); // Dara un salto de línea entre cada fila.
        }
        System.out.println();
    }
}
