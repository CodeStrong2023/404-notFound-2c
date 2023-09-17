import javax.swing.*;
import java.util.Scanner;

public class EjerciciosCiclos08JOptionPane {
    public static void main(String[] args) {

        int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));

        int i = 1;
        while (i <= num) {
            JOptionPane.showMessageDialog(null,i);
            i++;
        }

    }
}
