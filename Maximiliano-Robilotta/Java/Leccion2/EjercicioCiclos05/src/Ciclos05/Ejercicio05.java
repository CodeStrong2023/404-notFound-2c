/* Ejercicio 5: Realizar unn juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y
luego ir pidiendo números indicando "Es mayor" o 
"Es menor" según sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos.
 */
package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); // Esto genera un número aleatorio.
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un número MAYOR.");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un número MENOR.");
            }
            else{
                JOptionPane.showMessageDialog(null, "\t¡¡¡FELICIDADES!!! Has adivinado el número!!!");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "\tAdivinaste el número en "+conteo+" intentos.");
    }
    
}