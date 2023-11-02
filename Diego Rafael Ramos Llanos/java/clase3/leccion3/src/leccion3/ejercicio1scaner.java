/*Ejercicio 3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane*/
package leccion3;

import java.util.Scanner;

public class ejercicio1scaner {
    public static void main(String[] args) {
        float numero;
        do{
        Scanner sc= new Scanner(System.in);
        System.out.println("Digite el numero: ");
        numero=sc.nextFloat();
        float resultado=numero%2;
        if (resultado==0){
            System.out.println("El numero es par ");
        }else{
            System.out.println("El numero es impar ");
        }
        }while(numero!=0);
    }  
}
