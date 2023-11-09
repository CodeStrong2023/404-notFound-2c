package arreglos_ejercicio_15;

import java.util.Scanner;

public class Arreglos_Ejercicio_15 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int arreglo[]=new int[10];
        boolean creciente=true;
        int numero,numero2=0;
        System.out.println("llenar el arreglo: ");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.println(i+".digite un numero:");
                arreglo[i]=entrada.nextInt();
                
            }
            for (int i = 0; i < 9; i++) {
                if(arreglo[i]<arreglo[i+1]){
                    creciente=true;
                }
                if(arreglo[i]>arreglo[i+1]){
                    creciente=false;
                    break;
                }
                if(creciente==false){
                    System.out.println("\nEl arreglo esta desordenado.");
                    
                }
                
                
            }
        }while(creciente==false);
            
            System.out.println("\ndigite un numero para buscar en el arreglo:");
            numero=entrada.nextInt();
            int i=0;
            while(i<10 && arreglo[i]<numero){
                i++;
            }
            if(i==10){
                System.out.println("\nNumero no encontrado");
            }
            else{
                if(arreglo[i]==numero){
                    System.out.println("\nNumero encontrado en la posicion: "+i);
                }
                else{
                    System.out.println("numero no encontado");
                }
            }
            System.out.println();
        }
}

