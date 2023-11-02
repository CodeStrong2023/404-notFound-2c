/*Ejercicio 10: Pedir 10 números y escribir la suma
total
Hacerlo con la clase Scanner y JOptionPane*/
package leccion6;

import java.util.Scanner;

public class ejercicio2 {
    public static void main(String[] args) {
        int suma=0,num,contador=1;
        do{
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite el numero"+"para la suma: ");
        System.out.println("Contador: "+contador);
        num = sc.nextInt();
        suma+=num;
        contador++;
        }while(contador != 11);
         System.out.println("La suma es: " + suma);
    } 
   
    
}
