/*Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane*/
package leccion3;

import java.util.Scanner;

public class ejercicio2scaner {
    public static void main(String[] args) {
        float numero;
        int acumulador=-1;
        do{
        Scanner sc= new Scanner(System.in);
        System.out.println("Digite el numero: ");
        numero=sc.nextFloat();
        acumulador++;
        }while(numero>0);
        System.out.println("la cantidad acumulada es: "+ acumulador);
    }
}
