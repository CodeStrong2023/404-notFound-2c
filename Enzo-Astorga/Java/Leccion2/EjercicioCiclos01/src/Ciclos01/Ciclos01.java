/*
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir el proceso hasta que
se introduzca un número negativo.
*/
package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
         int numero, cuadrado;
         System.out.println("Digite un número: ");
         numero = Integer.parseInt(entrada.nextLine());
         while(numero >= 0) { // Mientras el número sea igual a 0 o positivo.
             cuadrado = (int)Math.pow(numero, 2); // Math.pow se utiliza para elevar un número a una potencia. En este caso, numero es la base y 2 es el exponente.
             System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
             System.out.println("Digite otro número: ");
             numero = Integer.parseInt(entrada.nextLine());
         }
         System.out.println("El programa ha finalizado por número negativo.");
        
    }
    
}
