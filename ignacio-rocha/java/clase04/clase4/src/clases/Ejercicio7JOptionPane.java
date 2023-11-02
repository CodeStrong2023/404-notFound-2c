package clases;

import javax.swing.JOptionPane;


public class Ejercicio7JOptionPane {
    public static void main(String[] args) {
        int numero,conteo=0,suma=0;
        float promedio=0;
        numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero!=0){ //mientras el numero no sea negativo
            suma+=numero;
            conteo++;
            numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        }
        if(conteo==0){
             JOptionPane.showMessageDialog(null,"\n error , la division entre cero no existe");
            
        }
        else{
            promedio=(float) suma/conteo;
            JOptionPane.showMessageDialog(null,"\n el promedio es: "+promedio);
        }
    }
}
