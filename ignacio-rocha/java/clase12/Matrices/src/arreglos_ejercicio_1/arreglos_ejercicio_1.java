/*ejercicio 1: leer 5 numeros, guardarlos en un arreglo y 
mostrarlos en el mismo orden introducido
*/
package arreglos_ejercicio_1;

import java.util.Scanner;

public class arreglos_ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        float[]arreglo=new float[5];
        System.out.println("guardando los datos en el arreglo: ");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+" digite un numero: ");
            arreglo[i]=entrada.nextFloat();
            
        }
        System.out.println("\nimprimir los datos del arreglo: ");
        for (float i : arreglo){
            System.out.println(i+" ");
        }
        System.out.println("\n");
    }
    
}
