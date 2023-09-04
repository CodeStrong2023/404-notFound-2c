import java.util.Random;
import java.util.Scanner;

public class EjerciciosConCiclos5Scanner {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int numRandom = 50;

        System.out.println("Se a generado un número random entre 0 y 100, ingrese un número para adivinarlo");
        int num = entrada.nextInt();

        while (num != numRandom) {
            if (num > numRandom) {
                System.out.println("El número que buscás es menor");
            } else {
                System.out.println("El número que buscás es mayor");
            }
            System.out.println("Ingresa otro numero: ");
            num = entrada.nextInt();
        }
        System.out.println("Encontraste el número!");
    }
}
