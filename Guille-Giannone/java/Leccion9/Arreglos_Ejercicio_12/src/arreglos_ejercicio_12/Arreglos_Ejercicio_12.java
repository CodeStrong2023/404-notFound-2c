/*
Ejercicio 12: Leer por teclado una tabla de 10 elementos numericos
enteros, en una posicion (entre 0 y 9). Eliminar el elemento situado en la 
posicion dada sin dejar huecos
*/
package arreglos_ejercicio_12;

import java.util.Scanner;


public class Arreglos_Ejercicio_12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int tabla[] = new int[10];
        int posicion, j=0;
        
        System.out.println("Llenar la tabla: ");
        for (int i = 0; i < 10; i++) {
            System.out.print(i+" .Digite un numero: ");
            tabla[i] = entrada.nextInt();
            }
        System.out.println("");
        do{
            System.out.println("Digite una posicion a eliminar entre 0 y 9: ");
            posicion = entrada.nextInt();
        }while(posicion < 0 || posicion >9);
        
        // Eliminando el elemento de la posicion indicada
        for (int i = posicion; i < 9; i++) {
            tabla[i] = tabla[i+1];
        }
        System.out.println("La tabla queda: ");
        for (int i = 0; i < 9; i++) {
            System.out.print(tabla[i]+"-");
        }
        System.out.println("");
    }
}
