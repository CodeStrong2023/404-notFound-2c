/*Ejercicio 6: Pedir números hasta que se teclee un O, mostrar
la suma de todos los números introducidos.*/
package persona;

import java.util.Scanner;

public class ejercicio1 {

    public static void main(String[] args) {
        int numero = -1, suma=0;
        Scanner cs = new Scanner(System.in);
        do {
            if (numero != 0) {
                System.out.println("Digite un numero y para finalizar digite un cero 0");
                numero = cs.nextInt();
                suma=suma+numero;
            } else {
                System.out.println("Saliste del programa");
            }
        } while (numero != 0);
        System.out.println("La suma de los numeros introducido es: " + suma );
    }

}
