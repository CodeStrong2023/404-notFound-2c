
package javaclase04;

import javax.swing.JOptionPane;

public class JavaClase04CiclosEjercicio01Pt2 {
    public static void main(String[] args) {
        int numero,suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            suma+= numero;
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, suma +"La suma de todos los números ingresados es: "+suma);
    }
}
