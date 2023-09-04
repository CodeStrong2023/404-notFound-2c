import javax.swing.*;
import java.util.Scanner;

public class EjerciciosConCiclos4JOptionPane {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

        int conteo = 0;
        while (num > 0){
            if (num != 0) {
                JOptionPane.showMessageDialog(null, "El numero " + num + " es positivo");
                conteo++;
            }
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero"));
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + conteo + " numeros que no son negativos");
    }
}