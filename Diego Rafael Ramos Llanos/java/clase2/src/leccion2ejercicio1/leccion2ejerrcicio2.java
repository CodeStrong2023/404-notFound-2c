/*Ejercicio 2: Leer un número e indicar si es positivo o
negativo. EI proceso se repetira hasta que se introduzca
un cero 0 */
package leccion2ejercicio1;

import javax.swing.JOptionPane;

public class leccion2ejerrcicio2 {
    public static void main(String[] args) {
        int numero;
        do{
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        if (numero<0){
            JOptionPane.showMessageDialog(null,"el numero es negativo");
        }else if(numero>0){
        JOptionPane.showMessageDialog(null,"el numero es positivo");
        }      
        }while(numero!=0);
    }
}
