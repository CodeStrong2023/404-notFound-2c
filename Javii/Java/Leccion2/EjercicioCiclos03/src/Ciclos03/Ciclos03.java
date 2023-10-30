/*
Ejercicio 3: Leer numeros hasta que se entroduzca un cero
Para cada uno indicae si es par o impar.
Primero lo haremos con clase escanner
Luego con la clase JOptionPane.
*/
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		int numero;
		System.out.println("Digite un numero: ");
		numero = Integer.parseInt(entrada.nextLine());
		while (numero != 0){
			if(numero % 2 == 0){
				System.out.println("El numero ingresado "+numero+" es Par");
			}
			else{
				System.out.println("El numero ingresado "+numero+" es Impar");
			}
			System.out.println("Digite otro numero: ");
			numero = Integer.parseInt(entrada.nextLine());
		}
		System.out.println("El numero ingresado es "+numero+" finaliza el programa");
	}
}
