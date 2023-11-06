/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han intraducido.
Lo hacemos primero con la clase scanner
Luego lo hacemos con la clase JOptionPane
 */


package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        
        int numero, conteo = 0;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero" +numero+ "es POSITIVO");
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado" +conteo+ "números que no son negativos");
      
    }
    
    
}
