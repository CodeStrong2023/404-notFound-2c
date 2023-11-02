package Ejercicio4;

import java.util.Scanner;

public class ejercicio4 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int numero,conteo=0;
        System.out.println("digite un numero: ");
        numero=Integer.parseInt(entrada.nextLine());
        while(numero>=0){
            System.out.println("el numero "+numero+" es POSITIVO");
            conteo++;
            System.out.println("digite otro numero: ");
            numero=Integer.parseInt(entrada.nextLine());
            
        }
        System.out.println("A ingresado "+conteo+" numeros que no son negativos");
    }
}
