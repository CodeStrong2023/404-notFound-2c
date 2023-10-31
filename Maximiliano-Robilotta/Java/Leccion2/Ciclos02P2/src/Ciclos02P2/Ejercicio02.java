/*
Ejercicio 2: Leer un número e indicar si es postitivo o negativo.
El proceso se repetirá hasta que se introduzca un 0.
 */
package Ciclos02P2;

import javax.swing.JOptionPane;

public class Ejercicio02 {
    public static void main(String[] args) {
        
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El número "+numero+" es positivo.");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número "+numero+" es negativo.");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        JOptionPane.showMessageDialog(null, "El número "+numero+" finaliza el programa.");
        
    }
    
}