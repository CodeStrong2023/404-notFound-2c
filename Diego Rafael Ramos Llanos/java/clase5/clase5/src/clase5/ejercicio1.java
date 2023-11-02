/*Ejercicio 8: Pedir un número N, y mostrar todos los números
del 1 al N*/
package clase5;

import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {
        int n,num=1;
        Scanner sc =new Scanner(System.in);
        System.out.println("Digite un numero: ");
        n=sc.nextInt();
        do{     
            System.out.print(num+" ");
            num++;
        }while(num!=n);
        System.out.println("");
        System.out.println("el numero introducido es: " + n);
    }
}
