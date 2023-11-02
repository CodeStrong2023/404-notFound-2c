/*ejercicio 1: leer un numero y mostrar su cuadrado,
repetir el proceso hasta que se introduzca un numero negativo
*/
package Ciclos01;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos01 {
    public static void main(String[] args) {
       /* Scanner entrada = new Scanner(System.in);
        int numero, cuadrado;
        numero=Integer.parseInt(entrada.nextLine());
        while(numero>=0){ //mientras el numero sea igual a cero o positivo
            cuadrado=(int)Math.pow(numero,2);
            System.out.println("el numero: "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("digite otro numero: ");
            numero=Integer.parseInt(entrada.nextLine());
        }
*/
       
       int numero,cuadrado;
       numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
       while(numero>=0){
           cuadrado=(int)Math.pow(numero,2);
           System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
           System.out.println("digite otro numero: ");
              numero=Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
       }
        System.out.println("el programa a finalizado por numero negativo");
       
    }
}
