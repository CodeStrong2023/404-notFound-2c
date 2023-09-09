/* Ejercicio 7: Pedir números hasta que se introduzca uno negativo
y calcular el promedio
 */
package Ciclos07;

import javax.swing.JOptionPane;


public class Ejercicio07 {

    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));

        while (numero >= 0) { // Mientras el número no sea negativo.
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        if (conteo == 0) {
            JOptionPane.showMessageDialog(null, "Error, la división entre cero no existe");

        } else {
            promedio = (float) suma / conteo;
            JOptionPane.showMessageDialog(null, "El promedio es: " + promedio);

        }
    }

}
