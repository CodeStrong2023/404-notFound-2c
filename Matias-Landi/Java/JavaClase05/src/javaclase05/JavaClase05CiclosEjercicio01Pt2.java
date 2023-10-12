/*
Ejercicio 1: Pedir un número N, y mostrar todos los números del 1 al N.
*/
package javaclase05;

import javax.swing.JOptionPane;

public class JavaClase05CiclosEjercicio01Pt2 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        int i = 1;
        while( i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
}
