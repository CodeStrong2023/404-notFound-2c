/*
Leer dos series de 10 enteros, que estarán ordenados crecientemente.
Copiar(fusionar) las dos tablas en una tercera, de forma que sigan ordenados.
 */
package ejerciciosvacaciones2dosemestre;

import java.util.Scanner;

public class Ej6 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int a[] = new int[10];
        int b[] = new int[10];
        int c[] = new int[20];
        boolean creciente = true;

        System.out.println("Llenar el primer arreglo: ");
        do {
            for (int i = 0; i < 10; i++) {
                System.out.println((i + 1) + ". Digite un número: ");
                a[i] = entrada.nextInt();
            }

            // Comprobamos si el arreglo está ordenado
            for (int i = 0; i < 9; i++) {
                if (a[i] < a[i + 1]) { // Creciente 1,2,3
                    creciente = true;
                } else {
                    if (a[i] > a[i + 1]) { // Dereciente 3,2,1
                        creciente = false;
                        break;
                    }
                }
                
                if(creciente == false){
                    System.out.println("\nEl arreglo está desordenado, vuelva a digitar: ");
                }
            }
        }while(creciente == false);
        
        System.out.println("Llenar el segundo arreglo: ");
        do{
            for(int i = 0; i < 10; i++){
                System.out.println((i + 1) + ". Digite un número: ");
                b[i] = entrada.nextInt();
            }
            
            for(int i = 0; i < 9; i++){
                if(b[i] < b[i+1]){
                    creciente = true;
                }
                if(b[i] > b[i+1]){
                    creciente = false;
                    break;
                }
            }
            
            if(creciente == false){
                System.out.println("\nEl arreglo está desordenado, vuelva a digitar: ");
            }
        }while(creciente == false);
        
        int i = 0; // iterador para el arreglo a.
        int j = 0; // iterador para el arreglo b.
        int k = 0; // iterador para el arreglo c.
        
        while(i < 10 && j < 10){
            if(a[i] < b[j]){ // Si el elemento es menor de b.
                c[k] = a[i]; // Copiamos el elemento de a.
                i++; // Avanzamos en una posición en a.
            }
            else{
                c[k] = b[j]; // Copiamos el elemento de b.
                j++; // Avanzamos una posición mas en b.
            }
            k++; // Avanzamos una posición más en c.
        }
        
        // Cuando salimos del while es por qué un arreglo (a o b), se ha copiado completamente
        if(i == 10){ // Significa que ya copiamos todo el arreglo a, falta el b.
            while(j < 10){ // Mientras el iterador sea menor a 10.
                c[k] = b[j]; // Copiamos el elemento de b en c.
                j++; // Avanzamos una posición en b.
                k++; // Avanzamos una posición en c.
            }
        }
        else{ // Significa que ya copiamos todo el arreglo b, falta el a.
            while(i < 10){
                c[k] = a[i];
                i++;
                k++;
            }
        }
    
        System.out.println("\nEl arreglo c completo es: ");
        for(k = 0; k < 20; k++){
            System.out.println(c[k]+" - ");
        }
        System.out.println();
    }

}
