package clases;

import java.util.Scanner;

public class ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma=0;
        do{
            System.out.println("digite un numero: ");
            numero=Integer.parseInt(entrada.nextLine());
            suma+=numero;
        }while(numero!=0);
        System.out.println("\nLa suma de todos los numeros ingresados es: "+suma);
    }
}
