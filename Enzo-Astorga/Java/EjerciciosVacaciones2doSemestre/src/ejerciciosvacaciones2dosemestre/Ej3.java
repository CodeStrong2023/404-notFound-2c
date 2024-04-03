/*
Leer 5 elementos numéricos que se introducirán ordenados de forma
creciente. Éstos los guardaremos en una tabla de tamaño 10. Leer un número N,
e insertarlo en el lugar adecuado para que la tabla continúe ordenada.
 */
package ejerciciosvacaciones2dosemestre;

import java.util.Scanner;

public class Ej3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int [10];
        boolean creciente = true;
        int numero, sitio_num = 0, j = 0;
        
        System.out.println("Llenar el arreglo: ");
        do{
            // Llenando el arreglo
            for(int i = 0; i < 5; i++){
                System.out.println((i+1)+". Digite un número: ");
                arreglo[i] = entrada.nextInt();
            }
            
            // Comprobar si el arreglo está ordenado en orden creciente
            for(int i = 0; i < 4; i++){
                if(arreglo[i] < arreglo[i+1]){ // Creciente 1,2,3
                    creciente = true;
                }
                if(arreglo[i] > arreglo[i+1]){
                    creciente = false;
                    break;
                }
            }
            
            if(creciente == false){
                System.out.println("\nEl arreglo no está ordenado en forma creciente, vuelva a digitar.\n");
            }
            
        }while(creciente == false);
        
        System.out.println("Digite un número a insertar: ");
        numero = entrada.nextInt();
        
        // Esto es para darnos cuenta en que posición va el número
        while(arreglo[j] < numero && j < 5){
            sitio_num++;
            j++;
        }
        
        // Por último, trasladamos una posición en el arreglo a los elementos que van detrás del número
        for(int i = 4; i >= sitio_num; i--){
            arreglo[i+1] = arreglo[i];
        }
        
        // Insertamos el número
        arreglo[sitio_num] = numero;
        
        System.out.println("\nEl arrelgo queda: ");
        for(int i = 0; i < 6; i++){
            System.out.println(arreglo[i] + " - ");
        }
        System.out.println();
    }
    
}
