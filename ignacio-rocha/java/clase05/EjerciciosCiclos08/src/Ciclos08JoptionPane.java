
import javax.swing.JOptionPane;

//ejercicio 8: pedir un numero N, y mostrar todos los numeros 
//del 1 al N

public class Ciclos08JoptionPane {
    public static void main(String[] args) {
        int numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        
         int i=1;
        while (i<=numero){
            JOptionPane.showMessageDialog(null,i);
            i++;
        }
    }
}
