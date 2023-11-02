package Ejercicio4;

import javax.swing.JOptionPane;

public class Ejercicio4JOptionPane {

    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while (numero >= 0) {
            JOptionPane.showMessageDialog(null,"el numero " + numero + " es POSITIVO");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        }
        JOptionPane.showMessageDialog(null,"A ingresado " + conteo + " numeros que no son negativos");
    }

}
