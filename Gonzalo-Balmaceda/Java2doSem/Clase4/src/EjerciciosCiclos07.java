import java.util.Scanner;

public class EjerciciosCiclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int num, suma = 0, conteo = 0;
        float promedio = 0;

        System.out.println("Ingrese un número: ");
        num = entrada.nextInt();

        while (num >= 0) {
            suma += num;
            conteo++;
            System.out.println("Digite otro número: ");
            num = entrada.nextInt();
        }

        if (conteo == 0) {
            System.out.println("Error!, La división entre cero no existe");
        } else {
            promedio = (float) suma/conteo;
        }
        System.out.println("promedio = " + promedio);
    }
}
