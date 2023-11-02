/*ejercicio 1: leer 5 numeros, guardarlos en un arreglo y 
mostrarlos en el mismo orden introducido
*/
package ejercicios;
import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {

        float[] numeros = new float[5];

        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            System.out.print("Introduce el número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }
        System.out.println("Los números introducidos son:");
        for (int i = 0; i < 5; i++) {
            System.out.println(numeros[i]);
        }

        scanner.close();//aca cierro el scanner 
    }
}