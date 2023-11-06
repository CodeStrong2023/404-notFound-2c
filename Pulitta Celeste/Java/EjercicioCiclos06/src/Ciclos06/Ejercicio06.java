/*
Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar
la suma de todos los números introducidos.
*/
package Ciclos06;

import javax.swing.JOptionPane;


public class Ejercicio06 {
    public static void main(String[] args) {
        
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            suma += numero;
        }while (numero != 0);
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros inresados es: " +suma);
    }
    
}
