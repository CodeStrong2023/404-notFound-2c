package arreglos_ejercicio_3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
           /*
        Ejercicios 3 = Leer 5 números, guardarlos en un arreglo y mostrarlos
        en el orden inverso.
        */

        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float numPositvo = 0, numNegativo = 0, mediaPositivos, mediaNegativos;
        float conteoPositivos = 0, conteoNegativos = 0, conteoCeros = 0;

        for (int i = 0; i < 5; i++) {
            System.out.println((i+1) + ". Ingrese un número: ");
            numeros[i] = entrada.nextFloat();

            // Realizamos el conteo dependiendo si es positivo, negativo o igual a cero.
            if (numeros[i] > 0) {
                numPositvo += numeros[i];
                conteoPositivos++;
            } else if (numeros[i] < 0) {
                numNegativo += numeros[i];
                conteoNegativos++;
            } else {
                conteoCeros++;
            }
        }

        // Mostramos los números ingresados en el arreglo
        System.out.println("\nLos números ingresados en el arreglo son: ");
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]);
        }

        // Mostramos el conteo y la media de los números positivos, negativos y los que son iguales a cero.
        System.out.println("\n");
        if (conteoPositivos == 0) {
            System.out.println("No se ingresaron números positivos, no se pueda sacar la media");
        } else {
            mediaPositivos = numPositvo/conteoPositivos;
            System.out.println("La cantidad de números positivos es: " + conteoPositivos + " con una media de: " + mediaPositivos);
        }

        if (conteoNegativos == 0) {
            System.out.println("No se ingresaron números negativos, no se pueda sacar la media");
        } else {
            mediaNegativos = numNegativo/conteoNegativos;
            System.out.println("La cantidad de números negativos es: " + conteoNegativos + " con una media de: " + mediaNegativos);
        }

        System.out.println("La cantidad de números iguales a cero es: " + conteoCeros);
        
    }
}
