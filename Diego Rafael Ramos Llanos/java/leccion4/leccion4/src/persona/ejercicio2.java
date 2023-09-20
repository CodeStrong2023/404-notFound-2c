/*Ejercicio 7: Pedir números hasta que se introduzca uno negativo
y calcular la media*/
package persona;

import java.util.Scanner;

public class ejercicio2 {
    public static void main(String[] args) {
        int numero, resultado = 0, contador = 0;
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println("Digite un numero para luego sumarse y sacar el promedio: ");
            numero = sc.nextInt();
            if (numero > 0) { 
                resultado += numero;
                contador++;
            }
        } while (numero >=0);
        float media =(float) resultado / contador; 
        if(contador==0){
            System.out.println("ERROR LA DIVICION ENTRE CERO NO EXIXTE");
        }else{
        System.out.println("La media es: " + media);
        }
    }
}
