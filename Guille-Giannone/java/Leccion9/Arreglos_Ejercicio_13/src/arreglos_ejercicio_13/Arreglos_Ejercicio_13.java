/*
Ejercicio 13: Leer 10 numeros en una tabla. Guardar en otra
tabla los elementos pares de la primera, y a continuacion los impares.
*/
package arreglos_ejercicio_13;

import java.util.Scanner;

public class Arreglos_Ejercicio_13 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        int tabla[] = new int [10];
        int conteo_pares = 0, conteo_impares = 0;
        
        System.out.println("Llenar tabla: ");
        for (int i = 0; i < 10; i++) {
            System.out.print((i+1)+" .Digite un numero: ");
            tabla[i] = entrada.nextInt();
            if(tabla[i] % 2 == 0){
                conteo_pares ++;
            }
            else{
                conteo_impares ++;
            }
        }
        // Creamos los arreglos pares e impares
        int par[] = new int [conteo_pares];
        int impar[] = new int [conteo_impares];
        
        conteo_pares = 0;  //Los usamos como iteradores
        conteo_impares = 0;
        
        for (int i = 0; i < 10; i++) {
            if(tabla[i] % 2 == 0){
                par[conteo_pares] = tabla[i];
                conteo_pares ++;
            }
            else{
                impar[conteo_impares] = tabla[i];
                conteo_impares ++;
            }
        }
        System.out.println("\nTabla ingresada: ");
        for (int i = 0; i < 10; i++) {
            System.out.print(tabla[i]+" - ");
        }
        System.out.println("\nTabla Pares: ");
        for (int i = 0; i < conteo_pares; i++) {
            System.out.print(par[i]+" - ");
        }
        System.out.println("\nTabla Impares: ");
        for (int i = 0; i < conteo_impares; i++) {
            System.out.print(impar[i]+" - ");
        }
        System.out.println("");
    }
    
}
