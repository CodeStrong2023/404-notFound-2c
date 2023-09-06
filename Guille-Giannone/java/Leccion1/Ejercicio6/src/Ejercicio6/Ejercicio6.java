
package Ejercicio6;

import java.util.Scanner;
public class Ejercicio6 {

   
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        float guillermo, luis, juan, total;
        System.out.println("Digite la cantidad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo/2;
        juan = (luis + guillermo)/2;
        total = luis + guillermo + juan;
        System.out.println("El dinero de Luis es: $"+luis);
        System.out.println("El dinero de Juan es: $"+juan);
        System.out.println("EL total de dinero entre los 3 es: "+total);
        
    }
    
}
