/*Ejercicio 1:Pedir npumeros hasta que se teclee un 0, msotrar
la suma de todos los números introducidos.
*/
package javaclase04;

import java.util.Scanner;

public class JavaClase04CiclosEjercicio01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero,suma = 0;
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma+= numero;
        }while(numero != 0);
        System.out.println("La suma de todos los números ingresados es: " +suma );        
    }
}
