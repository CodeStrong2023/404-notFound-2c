/*ejercicio 2:leer 5 numeros, guardarlos en un arreglo y 
mostrarlos en el orden inverso al introducido.
*/
package Arreglos_ejercicio_2;

import java.util.Scanner;

public class Arreglos_ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        float numeros[]=new float[5];
        System.out.println("guardando los elementos del arreglo: ");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+" digite un numero: ");
            numeros[i]=entrada.nextFloat();
                      
        }
        System.out.println("imprimimos los elementos del arreglo: ");
        for (int i = 4; i >=0; i--) {
            System.out.println(i+" "+numeros[i]);
            
        }
        System.out.println("\n");
    }
}
