/*Ejercicio 8: Pedir un número N, y mostrar todos los números
del 1 al N*/
package clase5;

import javax.swing.JOptionPane;

public class ejercicio1joptionpane {
    public static void main(String[] args) {
        int n,num=1;
        String input = JOptionPane.showInputDialog("Digite un numero: ");
        n = Integer.parseInt(input);
        StringBuilder output = new StringBuilder();
        do{
            output.append(num).append(" ");
            num++;
        }while(num!=n);
         JOptionPane.showMessageDialog(null, output.toString(), "Secuencia de Números", JOptionPane.INFORMATION_MESSAGE);
          JOptionPane.showMessageDialog(null, "El número introducido es: " + n, "Número Introducido", JOptionPane.INFORMATION_MESSAGE);
    }
}
