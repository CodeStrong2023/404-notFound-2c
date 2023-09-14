
package leccion2ejercicio1;

import javax.swing.JOptionPane;

public class ciclosejerc {
    public static void main(String[] args) {
        while (true){
        System.out.println(" ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número (ingrese un número negativo para salir):"));
        if (numero < 0){
            System.out.println("finaliza el programa por numero negativo");
            break;
        } 
        int resultado = (int) Math.pow(numero, 2);
        System.out.println("resultado = " + resultado);
        }
    }
    
}
