/*
Ejercicio 2: Crear una matriz de tamaño 7 x 7 y rellenarla de forma que los 
elementos de la diagonal principal sean 1 y el resto 0
*/
package ejercicio_matriz_02;

import java.util.Scanner;

public class EjercicioMatriz02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][] = new int [7][7];
        
        //Llenado de Matriz
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                if(i==j){
                    matriz[i][j] = 1;
                }
                else{
                    matriz[i][j] = 0;
                }
            }
        }
        //Mostramos matriz completa
        System.out.println("\nMostramos Matriz completa: ");
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        System.out.println("");
    }
}
