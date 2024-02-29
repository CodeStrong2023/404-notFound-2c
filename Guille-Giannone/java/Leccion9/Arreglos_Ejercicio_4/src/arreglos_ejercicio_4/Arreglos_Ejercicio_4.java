/*
Ejercicio 4: Leer 10 números enteros, guardarlos en un arreglo,
Debemos mostrarlos en el siguiente orden: el primero, el ultimo,
el segundo, el penultimo, el tercero, etc.
 */
package arreglos_ejercicio_4;

import java.util.Scanner;


public class Arreglos_Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        int numeros [ ] = new int [10];
        
        for (int i = 0; i < 10; i++) {
            System.out.print((i+1)+".Digite un numero: ");
            numeros[i] = entrada.nextInt();
        }
        System.out.println("El resultado es: ");
        for (int i = 0; i < 5; i++) {
            System.out.print(numeros[i]+" ");
            System.out.print(numeros[9-i]+" ");
        }
        System.out.println(" ");
    }
}
