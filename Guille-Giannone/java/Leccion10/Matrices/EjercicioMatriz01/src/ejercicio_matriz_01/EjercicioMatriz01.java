/*
Ejercicio 1: Crear una matriz de tamaño 3x3, transponerla y mostrarla 
*/
package ejercicio_matriz_01;

import java.util.Scanner;

public class EjercicioMatriz01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][] = new int [3][3];
        System.out.println("Rellenar Matriz");
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.print("Matriz["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println();
        
        System.out.println("Matriz Original: ");
        for (int i=0;i<3;i++){
            for (int j=0;j<3;j++){
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
        
        //Matriz Transpuesta
        System.out.println("Matriz Transpuesta");
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                System.out.print(matriz[j][i]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
