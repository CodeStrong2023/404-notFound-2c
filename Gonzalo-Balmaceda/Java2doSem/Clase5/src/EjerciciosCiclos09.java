import java.util.Scanner;

public class EjerciciosCiclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int dia, mes, anio;

        System.out.println("Ingrese el dia: ");
        dia = entrada.nextInt();

        System.out.println("Ingrese el mes: ");
        mes = entrada.nextInt();

        System.out.println("Ingrese el año: ");
        anio = entrada.nextInt();

        if ((dia != 0) && (dia <= 30) ) {
            if ((mes != 0) && (mes <= 30)){
                if ((anio != 0) && (anio <= 2023)) {
                    System.out.println("La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    System.out.println("Error, año no valido");
                }
            } else {
                System.out.println("Error, mes no valido");
            }
        } else {
            System.out.println("Error, dia no valido");
        }
    }
}
