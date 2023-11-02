/*Ejercicio 3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane*/
package leccion3;

import javax.swing.JOptionPane;

public class ejercicio1joption {
    public static void main(String[] args) {
        float numero;
        do{
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        if (numero==0){
            break;
        }
        float resultado=numero%2;
        if (resultado==0){
            JOptionPane.showMessageDialog(null,"el numero es par: ");
            System.out.println(" ");
        }else{
            JOptionPane.showMessageDialog(null,"el numero es impar: ");
            System.out.println(" ");
        }
        }while(numero!=0);
        JOptionPane.showMessageDialog(null,"el numero es 0: se finaliza el programa");
    }
    
}
