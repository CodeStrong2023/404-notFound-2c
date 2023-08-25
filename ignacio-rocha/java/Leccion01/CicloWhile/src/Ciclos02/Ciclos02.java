/*ejercicio 2: leer un numero e indicar si es positivo o negativo.
el proceso se repetira hasta que se introduzca un cero 0
*/
package Ciclos02;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        /*Scanner entrada=new Scanner (System.in);
        System.out.println("digite un numero: ");
        int numero=Integer.parseInt(entrada.nextLine());
        while(numero!=0){
            if(numero>0){
                System.out.println("el numero "+numero+" es POSITIVO");
            }
            else{
                System.out.println("el numero "+numero+" es NEGATIVO");
            }
              System.out.println("digite un numero: ");
        numero=Integer.parseInt(entrada.nextLine());
      
        }*/
        int numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero!=0){
            if(numero>0){
                JOptionPane.showInputDialog(null,"el numero "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showInputDialog(null,"el numero "+numero+" es NEGATIVO");
            }
            numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        }
    }
}
