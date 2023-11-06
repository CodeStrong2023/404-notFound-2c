/*
Ejercicio 1: Leer un númeor y mostrar su cuadrado, repetir el preoceso
hasta que se introduzca un número negatic
*/
package Ciclos001;

import java.util.Scanner;


public class Ciclos001 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, cuadrado;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+"elevado al cuadradoes: "+cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por negativo");
    }
    
    
}
