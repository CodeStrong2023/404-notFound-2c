
package persona;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio2JOptionpane {
        public static void main(String[] args) {
        int numero, resultado = 0, contador = 0;
        float media;
        Scanner sc = new Scanner(System.in);
        do {
            numero=Integer.parseInt(JOptionPane.showInputDialog("Digite un numero y para finalizar digite un cero 0"));
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
