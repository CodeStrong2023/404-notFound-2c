/*Ejercicio 7: Pedir números hasta que se introduzca uno negativo
y calcular la media*/
package persona;

import javax.swing.JOptionPane;

public class ejercicio2JOptionpane {
        public static void main(String[] args) {
        int numero, resultado = 0, contador = 0;
        float media;
        do {
            numero=Integer.parseInt(JOptionPane.showInputDialog("Digite un numero para luego sumarse y sacar el promedio: "));
            if (numero > 0) { 
                resultado += numero;
                contador++;
            }
        } while (numero >=0);
        media = (float)resultado / contador; 
        if(contador==0){
            JOptionPane.showMessageDialog(null,"ERROR LA DIVICION ENTRE CERO NO EXIXTE");
        }else{
        JOptionPane.showMessageDialog(null,"La media es: " + media);
        }
    }
}
