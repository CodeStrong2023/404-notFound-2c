/*Ejercicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma
de cada fila y de cada columna.*/
package ejercicios;

import java.util.Scanner;

public class ejercicio3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingrese el número de filas (n): ");
        int n = entrada.nextInt();
        System.out.print("Ingrese el número de columnas (m): ");
        int m = entrada.nextInt();

        int matriz[][] = new int[n][m];

        System.out.println("Ingrese los valores de la matriz:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print("matriz[" + i + "][" + j + "]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }

        System.out.println("Matriz ingresada:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }

        for (int i = 0; i < n; i++) {
            int sumaFila = 0;
            for (int j = 0; j < m; j++) {
                sumaFila += matriz[i][j];
            }
            System.out.println("Suma de la fila " + i + ": " + sumaFila);
        }
        for (int j = 0; j < m; j++) {
            int sumaColumna = 0;
            for (int i = 0; i < n; i++) {
                sumaColumna += matriz[i][j];
            }
            System.out.println("Suma de la columna " + j + ": " + sumaColumna);
        }
    }
}
