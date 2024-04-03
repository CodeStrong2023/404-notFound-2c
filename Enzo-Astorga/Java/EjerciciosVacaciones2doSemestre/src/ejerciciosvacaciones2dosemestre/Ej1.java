/*
Leer 10 números enteros, guardarlos en un arreglo. Debemos mostrarlos
en el siguiente orden: 
El primero, el último, el segundo, el penúltimo, el tercero, etc.
 */
package ejerciciosvacaciones2dosemestre;

import java.util.Scanner;

public class Ej1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int[10];
        
        for(int i = 0; i < 10; i++){
            System.out.println((i+1) + ". Digite un número: ");
            numeros[i] = entrada.nextInt();
        }
        
        System.out.println("El resultado es: ");
        for(int i = 0; i < 5; i++){
            System.out.println(numeros[i]+" "); // Primero, segundo
            System.out.println(numeros[9-i]+" "); // Últimos, penúltimo
        }
        System.out.println(); // Salto de línea
        
    }
    
}
