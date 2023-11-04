package matriz_ejercicio_05;

import javax.swing.*;
import java.util.Scanner;

public class ejercicio05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nColumnas, sumaFilas, sumaColumnas;
        int posFila, posColumna;

        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad de filas"));
        nColumnas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad de columnas"));

        matriz = new int[nFilas][nColumnas];
        int filas[] = new int[nFilas];
        int columnas[] = new int[nColumnas];


        System.out.println("Llenamos la matriz");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nColumnas; j++) {
                System.out.println("matriz["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println();

        System.out.println("Mostramos la matriz");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nColumnas; j++) {
                System.out.println(matriz[i][j]);
            }
            System.out.println();
        }
        System.out.println();

        // Suma de las filas.
        posFila = 0;
        for (int i = 0; i < nFilas; i++) {
            sumaFilas = 0;
            for (int j = 0; j < nColumnas; j++) {
                sumaFilas += matriz[i][j];
            }
            filas[posFila] = sumaFilas;
            posFila++;
        }

        // Suma de las columnas (cambiamos las iteraciones)
        posColumna = 0;
        for (int j = 0; j < nFilas; j++) {
            sumaColumnas = 0;
            for (int i = 0; i < nColumnas; i++) {
                sumaColumnas += matriz[i][j];
            }
            columnas[posColumna] = sumaColumnas;
            posColumna++;
        }

        // Mostramos la suma de las filas y columnas.
        System.out.println("La suma de las filas es:");
        for (int i = 0; i < nFilas; i++) {
            System.out.println(filas[i] + " - ");
        }

        System.out.println("La suma de las columnas es:");
        for (int i = 0; i < nColumnas; i++) {
            System.out.println(columnas[i]);
        }
    }
}
