package arreglos_ejercicio_5;

import java.util.Scanner;

public class Arreglos_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        int numeros1[]=new int[10];
        int numeros2[]=new int[10];
        int numeros3[]=new int[20];
        System.out.println("llenamos el primer arreglo: ");
        for (int i = 0; i < 10; i++) {
            System.out.println((i+1)+". digite un numero: ");
            numeros1[i]=entrada.nextInt();
            
            
        }
        System.out.println("llenamos el segundo arreglo");
        for (int i = 0; i < 10; i++) {
            System.out.println((i+1)+". digite un numero:");
            numeros2[i]=entrada.nextInt();
            
            
        }
        int j=0;
        for(int i=0;i<10;i++){
            numeros3[j]=numeros1[i];
            j++;
            numeros3[i]=numeros2[i];
            j++;
        }
        System.out.println("mostramos el tercer arreglo:");
        for(int i=0;i<20;i++){
            System.out.println(numeros3[i]+" ");
        }
        System.out.println();
    }
}
