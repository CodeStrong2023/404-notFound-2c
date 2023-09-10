import javax.swing.*;
import java.util.Scanner;

public class EjerciciosCiclos07JOptionPane {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int num, suma = 0, conteo = 0;
        float promedio = 0;

        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));

        while (num >= 0) {
            suma += num;
            conteo++;

            num = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));
        }

        if (conteo == 0) {
            JOptionPane.showMessageDialog(null,"Error!, La división entre cero no existe");
        } else {
            promedio = (float) suma/conteo;
        }
        JOptionPane.showMessageDialog(null, "promedio = " + promedio);
    }
}
