package clases;

import java.util.Scanner;

public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int numero,conteo=0,suma=0;
        float promedio=0;
        System.out.println("digite un numero: ");
        numero=Integer.parseInt(entrada.nextLine());
        while(numero!=0){ //mientras el numero no sea negativo
            suma+=numero;
            conteo++;
            System.out.println("digite un numero: ");
            numero=Integer.parseInt(entrada.nextLine());
        }
        if(conteo==0){
            System.out.println("\n error , la division entre cero no existe");
            
        }
        else{
            promedio=(float) suma/conteo;
            System.out.println("\n el promedio es: "+promedio);
        }
    }
}
