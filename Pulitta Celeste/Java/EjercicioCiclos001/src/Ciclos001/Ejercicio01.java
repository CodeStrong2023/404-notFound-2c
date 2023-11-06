/*
Ejercicio 1: Leer un númeor y mostrar su cuadrado, repetir el preoceso
hasta que se introduzca un número negatic
*/
package Ciclos001;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+"elevado al cuadradoes: "+cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        System.out.println("El programa a finalizado por negativo");
    }
}
