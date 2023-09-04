import javax.swing.*;

public class Ejercicio02_SinClaseScanner {
    public static void main(String[] args) {

        int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

        while (num != 0) {
            if (num > 0) {
                JOptionPane.showMessageDialog(null, "El numero " + num + " es positivo" );
            } else {
                JOptionPane.showMessageDialog(null, "El numero " + num + " es negativo" );
            }
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero " + num + " finaliza el programa" );

    }
}
