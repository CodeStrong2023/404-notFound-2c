/*
Ejercicio 7: Crear una matriz "marco" de 5x5; todos sus elementos
deden ser 0 salvo los de los bordes que deben ser 1. Mostrarla.
*/
package ejercicio_matriz_07;

import java.util.Scanner;


public class EjercicioMatriz07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][] = new int [5][5];
        
        System.out.println("Rellenando la matriz: ");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (i==0 || i==4){
                    matriz [i][j] = 1;
                }
                else if(j==0 || j==4){
                    matriz [i][j] = 1;
                }
                else{
                    matriz [i][j] = 0;
                }
            }
        }
        System.out.println("La matriz es: ");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        System.out.println("");
    }
}
