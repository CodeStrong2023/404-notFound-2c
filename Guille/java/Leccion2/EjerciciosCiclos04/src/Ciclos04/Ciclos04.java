/*
Ejercicio 4: Pedir numero hasta que se teclee un negativo,
y mostrar cuantos numero se han introducido.
Lo hacemos primero con clase Scanner,
Luego lo hacemos con JOptionPane.
*/
package Ciclos04;

import java.util.Scanner;


public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0){
            System.out.println("El numero "+numero+" es POSITIVO");
            conteo ++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresado "+conteo+" numero que no son negativos");
        
    }
    
}
