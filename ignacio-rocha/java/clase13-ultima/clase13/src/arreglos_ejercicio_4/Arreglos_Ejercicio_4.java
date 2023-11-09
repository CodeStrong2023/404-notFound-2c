package arreglos_ejercicio_4;

import java.util.Scanner;

/*
ej 4:leer 10 numeros enteros, guardarlos en un
arreglo. debemos mostrarlos en el siguiente orden:
el primero, el ultimo, el segundo, el penultimo,
el tercero, etc.
*/
public class Arreglos_Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int numeros[]=new int[10];
        for (int i = 0; i < 10; i++) {
            System.out.println((i+1)+". digite un numero: ");
            numeros[i]=entrada.nextInt();
            
            
        }
        System.out.println("El resultado es: ");
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]+" " );
            System.out.println(numeros[9-i]+" ");        
            
        }
        System.out.println();//salto de linea
    }
}
