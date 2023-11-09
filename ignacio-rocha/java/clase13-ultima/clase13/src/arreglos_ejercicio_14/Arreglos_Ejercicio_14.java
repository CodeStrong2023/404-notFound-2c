package arreglos_ejercicio_14;

import java.util.Scanner;

/*
ej 14: leer dos series de 10 enteros,
que estaran ordenados crecientemente.
copiar(fusionar) las dos tablas en una tercera,
de forma que sigan ordenados
*/
public class Arreglos_Ejercicio_14 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int a[]=new int[10];
        int b[]=new int [10];
        int c[]=new int[20];
        boolean creciente=true;
        System.out.println("llenar el primer arreglo:");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.println((i+1)+". digite un numero:");
                a[i]=entrada.nextInt();
                
            }
            //comprobamos si el arreglo esta ordenado
            for (int i = 0; i < 9; i++) {
                if(a[i]<a[i+1]){//creciente 1-2-3
                    creciente=true;
                }
                if(a[i]>a[i+1]){//decreciente 3-2-1
                    creciente=false;
                    break;
                }
            }
            if (creciente==false){
                System.out.println("\nEl arreglo esta desordenado.");
            }
        }while(creciente==false);
        int i=0;
        int j=0;
        int k=0;
        while(i<10 && j<10){
            if(a[i]<b[i]){
                c[k]=a[i];
                i++;
            }
            else{
                c[k]=b[j];
                j++;
            }
            k++;
            if(i==10){
                while(j<10){
                    c[k]=b[j];
                    j++;
                    k++;
                }
            }
            else{
                while(i<10){
                    c[k]=a[i];
                    i++;
                    k++;
                }
            }
            System.out.println("\nEl arreglo c completo es:");
            for (k = 0; k < 20; k++) {
                System.out.println(c[k]+" - ");
                
            }
            System.out.println();
        }
    }
}
