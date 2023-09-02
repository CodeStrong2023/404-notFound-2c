import javax.swing.*;
import java.util.Scanner;

public class EjerciciosConCiclos3ClaseJOptionPane {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

        while (numero != 0) {
            if (numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado es par");
            } else {
                JOptionPane.showMessageDialog(null, "El numero ingresado es impar");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero 0 finaliza el programa");
    }
}
