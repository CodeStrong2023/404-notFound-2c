/*EJERCICIO 1:Leer un número y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un número negativo*/
package leccion2ejercicio1;

import java.util.Scanner;

public class Leccion2ejercicio1 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        while (true){
        System.out.println(" ");
        System.out.println("ingrese el numero que desea que se muestre su cuadrado: ");
        int numero = sc.nextInt();
        if (numero < 0){
            System.out.println("finaliza el programa por numero negativo");
            break;
        } 
        int resultado = (int) Math.pow(numero, 2);
        System.out.println("resultado = " + resultado);
        }
    }
}
