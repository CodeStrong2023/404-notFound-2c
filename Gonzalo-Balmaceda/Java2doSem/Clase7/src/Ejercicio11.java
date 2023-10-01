import javax.swing.*;

public class Ejercicio11 {
    public static void main(String[] args) {

        long numero = 1;
        for (int i = 1; i <= 20; i += 2) {
            numero *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los numeros impares es = " + numero);
    }
}
