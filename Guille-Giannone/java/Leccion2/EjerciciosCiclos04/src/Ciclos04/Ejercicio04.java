/*
Ejercicio 4: Pedir numero hasta que se teclee un negativo,
y mostrar cuantos numero se han introducido.
Lo hacemos primero con clase Scanner,
Luego lo hacemos con JOptionPane.
*/
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado "+conteo+" numero que no son negativos");
    }
}
