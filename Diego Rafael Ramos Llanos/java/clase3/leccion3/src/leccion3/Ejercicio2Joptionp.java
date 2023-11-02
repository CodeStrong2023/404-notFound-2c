/*Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane*/
package leccion3;

import javax.swing.JOptionPane;

public class Ejercicio2Joptionp {
    public static void main(String[] args) {
        int numero=0;
        int contador = -1;
        do{ 
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        contador++;
        }while(numero>0);
        JOptionPane.showMessageDialog(null,"cantidad de datos ingresados: "+contador);
    }
}
