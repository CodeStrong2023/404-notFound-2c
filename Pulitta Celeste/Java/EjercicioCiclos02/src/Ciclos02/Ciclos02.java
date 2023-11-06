/*
 Ejercicio2: Leer un número e indicar si es positivo o
negativo. El proceso se repite hasta que se introduzca
un cero
Hacer este ejercicio en la clase Scanner,
luego hacerlo nuevamente con la clase JOption.Pane
 */
package Ciclos02;

import javax.swing.JOptionPane;




public class Ciclos02 {
    public static void main(String[] args) {
        
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showInputDialog(null, "El numero"+numero+"es POSITIVO" );
            }
            else{
                JOptionPane.showInputDialog(null, "El numero"+numero+"es NEGATIVO" );
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        JOptionPane.showInputDialog(null, "El número"+numero+"finaliza el programa");
    }
}
