/*Ejercicio 10: Pedir 10 números y escribir la suma
total
Hacerlo con la clase Scanner y JOptionPane*/
package leccion6;

import javax.swing.JOptionPane;

public class ejercicio2JoptionPane {
    public static void main(String[] args) {
        int suma=0,num,contador=1;
        do{
        String input = JOptionPane.showInputDialog("Digite el numero para la suma:"
                +"\n(contador): "+contador);
        num = Integer.parseInt(input);
        suma+=num;
        contador++;
        }while(contador != 11);
        JOptionPane.showMessageDialog(null,"La suma es: " + suma);
    } 
}
