package clases;

import javax.swing.JOptionPane;

public class ejercicio6JOptionPane {

    public static void main(String[] args) {
        int numero, suma = 0;
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog(suma));
            suma += numero;
        } while (numero != 0);
        JOptionPane.showMessageDialog(null, "la suma de todos los numeros ingresados es: " + suma);

    }
}
