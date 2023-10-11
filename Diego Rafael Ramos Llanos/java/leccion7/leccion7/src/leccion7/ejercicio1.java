/*Ejercicio 11: Diseñar un programa que muestre eI producto
de los 10 primeros números impares
Hacerlo con JOptionPane*/
package leccion7;

import javax.swing.JOptionPane;

public class ejercicio1 {
    public static void main(String[] args) {
        int num,mult=1;
        for(num=1;num<=20;num++){
            if (num % 2 !=0){
            mult*=num;
            }
        }
        JOptionPane.showMessageDialog(null,"La multiplicacion es: " + mult);
    }
}
