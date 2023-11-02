/*leer 5 numeros por teclado, almacenarlos en un 
arreglo y a continuacion realizar la media de los 
numeros positivos, la media de los negativos y contar 
el numero de ceros
 */
package ejercicios;

import java.util.Scanner;

public class ejercicio3 {

    public static void main(String[] args) {
        int[] numeros = new int[5];
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            System.out.print("Introduce el número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        int sumaPositivos = 0;
        int sumaNegativos = 0;
        int contadorCeros = 0;
        int contadorPositivos = 0;
        int contadorNegativos = 0;

        for (int i = 0; i < 5; i++) {
            if (numeros[i] > 0) {
                sumaPositivos += numeros[i];
                contadorPositivos++;
            } else if (numeros[i] < 0) {
                sumaNegativos += numeros[i];
                contadorNegativos++;
            } else {
                contadorCeros++;
            }
        }

        double mediaPositivos = (double) sumaPositivos / contadorPositivos;
        double mediaNegativos = (double) sumaNegativos / contadorNegativos;

        System.out.println("Media de números positivos: " + mediaPositivos);
        System.out.println("Media de números negativos: " + mediaNegativos);
        System.out.println("Cantidad de ceros: " + contadorCeros);

        scanner.close();
    }
}
