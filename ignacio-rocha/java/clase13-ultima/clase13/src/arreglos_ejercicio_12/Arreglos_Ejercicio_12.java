package arreglos_ejercicio_12;

import java.util.Scanner;

public class Arreglos_Ejercicio_12 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int arreglo[]=new int[10];
        int posicion,j=0;
        System.out.println("llenar el arreglo: ");
        for (int i = 0; i < 10; i++) {
             System.out.println(i+". digite un numero: ");
             arreglo[i]=entrada.nextInt();
            
        }
        System.out.println();
        do{
            System.out.println("digite una posicion a eliminar: ");
            posicion=entrada.nextInt();
            
        }while(posicion<0||posicion>9);
        //eliminando el elemento de posicion indicada
        for (int i = posicion; i < 9; i++) {
            arreglo[i]=arreglo[i+1];
            
        }
        System.out.println("\nEl arreglo queda: ");
        for (int i = 0; i < 9; i++) {
            System.out.println(arreglo[i]+"-");
            
        }
        System.out.println();
        
    }
        
    
}
