/*
Ejercicio 2: Leer 5 numeros, guardarlos en un arreglo y
mostrarlos en un orden inverso al introducido
*/

package arreglos_ejercicio_2;

import java.util.Scanner;


public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] arreglos = new float[5];
        System.out.println("Guardando los datos en el arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+". Digite un numero: ");
            arreglos[i] = entrada.nextFloat();
    }
        System.out.println("\nImprimir los elementos del arreglo");
        for (int i = 4; i >= 0; i--) {
            System.out.println(i+" "+ arreglos[i]);
        }
        System.out.println("\n");
    }       
    
}