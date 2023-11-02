/*Ejercicio 12: Pedir un número y calcular su factorial
Hacerlo con las dos clases, Scanner y JOptionPane*/
package leccion7;

//import java.util.Scanner;
import javax.swing.JOptionPane;

public class ejercicio2 {
        public static void main(String[] args) {
        //Scanner scanner = new Scanner(System.in);
        int numero=Integer.parseInt(JOptionPane.showInputDialog("Ingresa un número para calcular su factorial: "));
       // System.out.print("Ingresa un número para calcular su factorial: ");
        //int numero = scanner.nextInt();
       // scanner.close();//cerrar scaner es una buena practica

        long factorial = 1;

        // Calcula el factorial utilizando un bucle for
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null,"El factorial de " + numero + " es " + factorial);
       // System.out.println("El factorial de " + numero + " es " + factorial);
    }
}
