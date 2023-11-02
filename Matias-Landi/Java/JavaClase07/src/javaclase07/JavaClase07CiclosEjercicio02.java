/*
Ejercicio 12: pedir un número y calcular su factorial
Hacerlo con las dos clases, Scanner y JOptionPane
 */
package javaclase07;


//import java.util.Scanner;
import javax.swing.JOptionPane;


public class JavaClase07CiclosEjercicio02 {
    public static void main(String[] args) {
       // Scanner entrada = new Scanner(System.in);
       long factorial = 1;
       //System.out.printIn("Digite un número: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        for(int i=1; i<=numero;i++){
            factorial *= i;
        }
        //System.out.printIn("\nEl factorial del número ingresado es: "+factorial);
        JOptionPane.showMessageDialog(null, "El factorial del número ingresado es: "+factorial);
                
    }
            
    
}
