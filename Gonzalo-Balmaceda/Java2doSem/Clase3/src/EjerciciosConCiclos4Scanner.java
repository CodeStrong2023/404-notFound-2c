import java.util.Scanner;

public class EjerciciosConCiclos4Scanner {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un numero");
        int num = entrada.nextInt();

        int conteo = 0;
        while (num >= 0){
            System.out.println("El numero " + num + " es positivo");
            conteo++;

            System.out.println("Ingrese otro numero");
            num = entrada.nextInt();
        }
        System.out.println("A ingresado " + conteo + " numeros que no son negativos");
    }
}
