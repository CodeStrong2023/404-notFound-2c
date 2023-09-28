
package javaclase02;

import java.util.Scanner;


public class JavaClase02CiclosEjercicio01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, cuadrado;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){ //Mientras el npumero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
     System.out.println("El programa a finalizado por número negativo");
                
    }
    
}
