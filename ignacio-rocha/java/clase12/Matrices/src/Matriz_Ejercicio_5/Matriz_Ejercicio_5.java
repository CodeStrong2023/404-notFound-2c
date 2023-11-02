//ej 5: crear y cargar una matriz de tamano nxm, mostrar la suma de 
//cada fila y de cada columna
package Matriz_Ejercicio_5;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int matriz[][],nFilas,sumaFilas,sumaCol,nCol;
        int posFila,posCol;
        nFilas=Integer.parseInt(JOptionPane.showInputDialog("ingrese fila:"));
        nCol=Integer.parseInt(JOptionPane.showInputDialog("ingrese columna:"));
        matriz=new int[nFilas][nCol];
        int filas[]=new int[nFilas];
        int columnas[]=new int[nCol];
        
        System.out.println("rellenando la matriz: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print("matriz ["+i+"]["+j+"]:");
                matriz[i][j]=entrada.nextInt();
                
                
            }
 
        }
        System.out.println("\nmatriz original: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.println(matriz[i][j]+"");
                
            }
            System.out.println("");
            
        }
    }
}
