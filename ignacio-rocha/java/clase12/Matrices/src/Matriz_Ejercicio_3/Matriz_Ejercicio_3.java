package Matriz_Ejercicio_3;

import java.util.Scanner;
//ejer 3: crear y cargar una matriz de 3x3 , transponerla y mostrarla

public class Matriz_Ejercicio_3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int[3][3];
        System.out.println("rellenar la matriz: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("matriz[" + i + "][" + j + "]");
                matriz[i][j] = entrada.nextInt();

            }

        }
        System.out.println();
        System.out.println("matriz original: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println(matriz[i][j] + " ");

            }
            System.out.println();
        }
        System.out.println();
        //matriz transpuesta
        System.out.println("matriz transpuesta: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println(matriz[j][i]+"");
                
            }
            
        }
    }

}

