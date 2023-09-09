/*
Ejercicio 7: Pedir numeros hasta que se introduzca un negativo
y calcular el promedio
*/
package Ciclos07;

import javax.swing.JOptionPane;


public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){ //Mientras que no sea negativo
            suma += numero;
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null, "Error, la division entre ceros no exite");
        }
        else{
            promedio = suma/conteo;
            JOptionPane.showMessageDialog(null,"El promedio es: "+promedio );
        }
    }
}
