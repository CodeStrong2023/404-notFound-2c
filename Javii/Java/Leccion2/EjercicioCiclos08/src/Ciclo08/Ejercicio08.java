/*
Ejercicio: Pedir un numero N, y mostrar todos los numeros desde el 1 a N
*/
package Ciclo08;

import javax.swing.JOptionPane;

public class Ejercicio08 {
	public static void main(String[] args) {
		int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
		int i = 1;
		while (i <= numero){
			JOptionPane.showMessageDialog(null, i);
			i++;
		}
	}
}
