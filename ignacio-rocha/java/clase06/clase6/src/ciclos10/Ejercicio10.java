package ciclos10;

import javax.swing.JOptionPane;


public class Ejercicio10 {
    public static void main(String[] args) {
        int numero,suma=0;
        for (int i = 1; i < 10; i++) {
            System.out.println("digite un numero: ");
            numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
            suma+=numero;
        }
        JOptionPane.showMessageDialog(null,"\nLa suma total es: "+suma);
    }
}
