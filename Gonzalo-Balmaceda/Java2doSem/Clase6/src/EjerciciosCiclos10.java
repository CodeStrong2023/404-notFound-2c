import java.util.Scanner;

public class EjerciciosCiclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num, suma = 0;

        for (int i = 1; i <= 10; i++) {
            System.out.println("Ingrese un número: ");
            num = entrada.nextInt();
            suma += num;
        }
        System.out.println("La suma de todos los números ingresado es : " + suma);
    }
}
