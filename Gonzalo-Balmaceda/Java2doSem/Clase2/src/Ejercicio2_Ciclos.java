import java.util.Scanner;

public class Ejercicio2_Ciclos {
    public static void main(String[] args) {

        // Ingresar un numero e indicar si es positivo o negativo.
        // el proceso se repetira hasta que se ingrese un 0

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrse un numero: ");
         int num = entrada.nextInt();

         while (num != 0) {
             if (num > 0) {
                 System.out.println("El numero ingresado " + num + " es positivo");
             } else {
                 System.out.println("El numero ingresado " + num + " es negativo");
             }
             System.out.println("Ingrese otro numero: ");
             num = entrada.nextInt();
         }
        System.out.println("El numero " + num + " finaliza el programa");
    }
}
