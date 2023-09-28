/*Ejercicio 2: Leer un número e indicar si es positivo o negativo.
El proceso se repetirá hasta que se introduzca un cero*/

package javaclase02;

import java.util.Scanner;


public class JavaClase02CiclosEjercicio02 {
    public static void main(String[]args){
    Scanner entrada = new Scanner(System.in);
System.out.println("Digite un número: ");
    var numero = Integer.parseInt(entrada.nextLine());
    while(numero != 0){
        if(numero > 0){
            System.out.println("El número "+numero+" es POSITIVO");
        }
        else{
            System.out.println("El numero "+numero+" es NEGATIVO");
        }
        System.out.println("Digite otro número: ");
        numero = Integer.parseInt(entrada.nextLine());
    }
        System.out.println("El número "+numero+" finaliza el programa");
       
    }
    }

