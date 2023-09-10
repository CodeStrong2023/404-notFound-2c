import java.util.Scanner;

public class EjerciciosCiclos06 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int num, suma = 0;

        do {
            System.out.println("Ingrese un numero: ");
            num = entrada.nextInt();
            suma += num;
        } while (num != 0);

        System.out.println("La suma de los numero ingresados es de " + suma);
    }
}
