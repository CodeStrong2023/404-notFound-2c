import java.util.Scanner;

public class Ejercicio1_Ciclos {
    public static void main(String[] args) {
        // Leer un numero y mostrar su cuadrado, repetir hasta que se ingrese
        // un numero negativo.

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un numero: ");
        int num = entrada.nextInt();

        int cuadrado = 0;
       while (num >= 0){
           cuadrado = (int)Math.pow(num, 2);
           System.out.println("El numero " + num + " elevado al cuadrado es " + cuadrado);

           System.out.println("Ingrese otro numero: ");
           num = entrada.nextInt();
       }
        System.out.println("Programa finalizado por que se ingreso un numero negativo");
    }
}
