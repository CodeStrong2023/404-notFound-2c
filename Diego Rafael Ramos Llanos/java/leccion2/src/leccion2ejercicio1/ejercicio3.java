/*Ejercicio 2: Leer un número e indicar si es positivo o
negativo. EI proceso se repetira hasta que se introduzca
un cero 0 .
Hacer este eiercicio con la clase Scanner.
luego hacerlo nuevamente con la clase JOptionPan*/
package leccion2ejercicio1;

import java.util.Scanner;

public class ejercicio3 {
    public static void main(String[] args) {
        int numero;
        do{
        Scanner sc=new Scanner(System.in); 
        System.out.println("Digite un numero: ");
        numero=sc.nextInt();
            if (numero<0){
                System.out.println("el numero es negativo");
            }else{
                System.out.println("el numero es positivo");
            }
        }while(numero!=0);
        }
    }
