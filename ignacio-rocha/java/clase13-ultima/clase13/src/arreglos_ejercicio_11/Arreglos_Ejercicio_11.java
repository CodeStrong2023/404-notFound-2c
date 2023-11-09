package arreglos_ejercicio_11;

import java.util.Scanner;

/*
ej 11: leer 5 elementos numericos que se
introduciran ordenados de forma creciente
estos los guardaremos en una tabla de tamaño 10.
leer un numero N,
e insertarlo en un lugar adecuado para que la tabla
continue ordenada
*/
public class Arreglos_Ejercicio_11 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int arreglo[]=new int[10];
        boolean creciente=true;
        int numero,sitio_num=0,j=0;
        
        System.out.println("llenar el arreglo: ");
        do{
            //llenando el arreglo
            for (int i = 0; i < 5; i++) {
                System.out.println((i+1)+". digite un numero:");
                arreglo[i]=entrada.nextInt();
                
                
            }
            //comprobar si el arreglo esta ordenado
            for (int i = 0; i < 4; i++) {
                if(arreglo[i]<arreglo[i+1]){//creciente 1,2,3
                    creciente=true;
                }
                if(arreglo[i]>arreglo[i+1]){
                    creciente=false;
                    break;
                }
                
            }
            if(creciente==false){
                System.out.println(" \nel arreglo esta ordenado de forma creciente");
            }
            
        }while(creciente==false);
        System.out.println("digite un numero a insertar: ");
        numero=entrada.nextInt();
        
        //esto para darnos cuenta en que posicion vamos
        while(arreglo[j]<numero && j<5){
            sitio_num++;
            j++;
            
        //por ultimo trasladamos una posicion en el arreglo a los elementos que van
            for (int i = 4; i < sitio_num; i--) {
                arreglo[i+1]=arreglo[i];
                
            }
            //insertamos el numero
            arreglo[sitio_num]=numero;
            System.out.println("\nEl arreglo queda: ");
            for (int i = 0; i < 6; i++) {
                System.out.println(arreglo[i]+"-");
                
            }
            System.out.println();
        }
    }
}
