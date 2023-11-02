package Ejercicio05;

import java.util.Scanner;

public class ejercicio05 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int numero,aleatorio,conteo=0;
        aleatorio=(int)(Math.random()*100);
        do{
            System.out.println("digite un numero: ");
            numero=Integer.parseInt(entrada.nextLine());
            if(numero<aleatorio){
                System.out.println("digite un numero mayor ");
            }
            else if(numero>aleatorio){
                System.out.println("digite un numero menor ");
            }
            else{
                System.out.println("FELICIDADES!!! ADIVINASTE EL NUMERO");
            }
            conteo++;
        }
        while(numero!=aleatorio);
        System.out.println("adivinaste el numero en: "+conteo+" intentos");
    }
}
