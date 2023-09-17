import java.util.Scanner;

public class EjerciciosCiclos08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un número: ");
        int num = entrada.nextInt();

        int i = 1;
        while (i <= num) {
            System.out.println("i = " + i);
            i++;
        }

    }
}
