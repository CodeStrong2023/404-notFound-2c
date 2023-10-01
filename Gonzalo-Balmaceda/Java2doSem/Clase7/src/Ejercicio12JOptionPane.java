import javax.swing.*;
import java.util.Scanner;

public class Ejercicio12JOptionPane {
    public static void main(String[] args) {

        long num = Long.parseLong(JOptionPane.showInputDialog("Ingrese un número"));

        long factorial = 1;
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }

        JOptionPane.showMessageDialog(null, "El factorial del número ingresado es = " + factorial);
    }
}
