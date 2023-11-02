/*Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y
luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N
EI proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos*/
package leccion3;

import java.util.Random;
import java.util.Scanner;

public class ejercicio3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rm = new Random();
         int numeroAdivinar = rm.nextInt(101);
        int intentos = 0;
        boolean adivinado = false;

        System.out.println("¡Bienvenido al juego de adivinar el número!");
        while (!adivinado) {
            System.out.print("Adivina el número (entre 0 y 100): ");
            int numeroUsuario = sc.nextInt();
            intentos++;
            if (numeroUsuario < numeroAdivinar) {
                System.out.println("El número es mayor.");
            } else if (numeroUsuario > numeroAdivinar) {
                System.out.println("El número es menor.");
            } else {
                System.out.println("¡Felicidades! Adivinaste el número en " + intentos + " intentos.");
                adivinado = true;
            }
        }
    }
}
