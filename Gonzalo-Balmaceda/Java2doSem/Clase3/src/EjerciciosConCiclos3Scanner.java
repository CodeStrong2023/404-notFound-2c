import java.util.Scanner;

public class EjerciciosConCiclos3Scanner {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un numero: ");
        int numero = entrada.nextInt();

        while (numero != 0) {
            if (numero % 2 == 0){
                System.out.println("El numero ingresado es par");
            } else {
                System.out.println("El numero es impar");
            }
            System.out.println("Ingrese otro numero: ");
            numero = entrada.nextInt();
        }
        System.out.println("El numero 0 termina el programa");
    }
}
