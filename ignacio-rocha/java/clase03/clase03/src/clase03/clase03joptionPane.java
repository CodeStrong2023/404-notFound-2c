package clase03;

import javax.swing.JOptionPane;


public class clase03joptionPane {
    public static void main(String[] args) {
        int numero;
        System.out.println("ingrese un numero: ");
        numero=Integer.parseInt(JOptionPane.showInputDialog("ingrese un numero: "));
        while(numero!=0){
            if(numero%2==0){
                JOptionPane.showMessageDialog(null,"el numero ingresado "+numero+" es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null,"el numero ingresado "+numero+" es IMPAR");
            }
            JOptionPane.showMessageDialog(null,"digite otro numero: ");
            numero=Integer.parseInt(JOptionPane.showInputDialog("ingrese un numero: "));
          
        }
        JOptionPane.showMessageDialog(null,"el numero: "+numero+" termino el programa");
    }
}
