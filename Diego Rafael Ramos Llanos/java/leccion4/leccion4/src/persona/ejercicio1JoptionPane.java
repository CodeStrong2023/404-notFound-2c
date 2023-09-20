
package persona;
import javax.swing.JOptionPane;

public class ejercicio1JoptionPane {
    public static void main(String[] args) {
        int numero = -1, suma=0;
        do {
            if (numero != 0) {
                numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero y para finalizar digite un cero 0"));
                suma=suma+numero;
            } else {
                System.out.println("Saliste del programa");
            }
        } while (numero != 0);
        JOptionPane.showMessageDialog(null,"La suma de los numeros introducido es: " + suma);
    }
    
}
