
package javaclase02;

import javax.swing.JOptionPane;

public class JavaClase02CiclosEjercicio01Pt02 {
    public static void main(String[] args) {
      int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){ //Mientras el npumero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
     System.out.println("El programa a finalizado por número negativo");   
        
    }
}
