/*
Leer 10 enteros en una tabla. Guardar en otra tabla los
elementos pares de la primera y a continuación los elementos impares.
 */
package ejerciciosvacaciones2dosemestre;

import java.util.Scanner;

public class Ej5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        int conteo_pares = 0, conteo_impares = 0;
        
        System.out.println("Llenar el arreglo: ");
        for(int i = 0; i < 10; i++){
            System.out.println((i + 1) + ". Digite un número: ");
            arreglo[i] = entrada.nextInt();
            
            if(arreglo[i] % 2 == 0){ // Contamos para crear los arrelgos.
                conteo_pares++;
            }
            else{
                conteo_impares++;
            }           
        }
        
        // Creamos los arreglos pares e impares
        int par[] = new int[conteo_pares];
        int impar[] = new int[conteo_impares];
        
        conteo_pares = 0; //Los usamos como iteradores
        conteo_impares = 0;
        
        for(int i = 0; i < 10; i++){
            if(arreglo[i] % 2 == 0){
                par[conteo_pares] = arreglo[i];
                conteo_pares++;
            }
            else{
                impar[conteo_impares] = arreglo[i];
                conteo_impares++;
            }
        }
        
        System.out.println("\nArreglo ingresado: ");
        for(int i = 0; i < 10; i++){
            System.out.println(arreglo[i]+" - ");
        }
        
        System.out.println("\nArreglo de pares: ");
        for(int i = 0; i < conteo_pares;i++){
            System.out.println(par[i]+" - ");
        }
        
        System.out.println("\nArreglo de impares: ");
        for(int i = 0; i < conteo_impares;i++){
            System.out.println(impar[i]+" - ");
            
        }
        System.out.println();
    }
    
}
