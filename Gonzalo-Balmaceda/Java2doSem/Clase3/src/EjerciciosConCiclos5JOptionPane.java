import javax.swing.*;
import java.util.Scanner;

public class EjerciciosConCiclos5JOptionPane {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        
        int numRandom = 50;

        int num = Integer.parseInt(JOptionPane.showInputDialog("Se a generado un número random entre 0 y 100, ingrese un número para adivinarlo"));

        while (num != numRandom) {
            if (num > numRandom) {
                JOptionPane.showMessageDialog(null,"El número que buscás es menor");
            } else {
                JOptionPane.showMessageDialog(null,"El número que buscás es mayor");
            }
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingresa otro numero"));
        }
        JOptionPane.showMessageDialog(null, "Encontraste el número!");
    }
}
