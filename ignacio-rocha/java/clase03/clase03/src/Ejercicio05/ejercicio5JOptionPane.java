package Ejercicio05;

import javax.swing.JOptionPane;

public class ejercicio5JOptionPane {
    public static void main(String[] args) {
        int numero,aleatorio,conteo=0;
        aleatorio=(int)(Math.random()*100);
        do{
            numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
            if(numero<aleatorio){
                JOptionPane.showMessageDialog(null,"digite un numero mayor ");
            }
            else if(numero>aleatorio){
                JOptionPane.showMessageDialog(null,"digite un numero menor ");
            }
            else{
                JOptionPane.showMessageDialog(null,"FELICIDADES!!! ADIVINASTE EL NUMERO");
            }
            conteo++;
        }
        while(numero!=aleatorio);
        JOptionPane.showMessageDialog(null,"adivinaste el numero en: "+conteo+" intentos");
    }
}
