/*
Ejercicio 3: Leer numeros hasta que se entroduzca un cero
Para cada uno indicae si es par o impar.
Primero lo haremos con clase escanner
Luego con la clase JOptionPane.
*/
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
	public static void main(String[] args) {
		int numero;

		numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
		while (numero != 0){
			if(numero % 2 == 0){
				JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es Par");
			}
			else{
				JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+" es Impar");
			}
			numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
		}
		JOptionPane.showMessageDialog(null, "El numero ingresado es "+numero+" finaliza el programa");
	}
}
