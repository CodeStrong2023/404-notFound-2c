
package javaclase03;

import javax.swing.JOptionPane;


public class CiclosEjercicio03Pt2 {
    public static void main(String[] args) {
         int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "El número ingresado es "+numero+" finaliza el programa");
    }
    
}
