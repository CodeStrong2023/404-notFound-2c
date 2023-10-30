/*
Ejercicio 10: Pedir 10 numeros y escribir la suma
total
Hacerlo con la clase Scanner y JOptionPane
*/
package ciclos10;

import javax.swing.JOptionPane;

public class Ejercicio10 {
	public static void main(String[] args) {
		int numero, suma = 0;
		for(int i = 1; i <= 10; i++){
			System.out.println("Digite un numero: ");
			numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
			suma += numero;
		}
		System.out.println("\nLa suma de todos los numeros es: "+suma);
		JOptionPane.showMessageDialog(null, "La suma de todos los numeros es: "+suma);
	}
}
