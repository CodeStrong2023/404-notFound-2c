import javax.swing.*;

public class EjerciciosCiclos06JOptionPane {
    public static void main(String[] args) {

        int num, suma = 0;

        do {
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
            suma += num;
        } while (num != 0);

        JOptionPane.showMessageDialog(null,"La suma de los numero ingresados es de " + suma);
    }
}
