
package ejercicios;
import java.util.Scanner;

public class Ejercicios {
    public static void main(String[] args) {
   //Ejercicio sacar Area y perimetro de un rectangulo
        
        var altoRectangulo = 5;
        var anchoRectangulo = 10;
        var perimetro = (altoRectangulo + anchoRectangulo)*2;
        var area = altoRectangulo * anchoRectangulo;
        System.out.println("perimetro = " + perimetro);
        System.out.println("area = " + area);
        
        //Ejercicio mostrar el numero mas grande
        
        Scanner scanner = new Scanner(System.in);
        int num1,num2,salida;
        System.out.println("Ingrese el primer numero");
        num1=scanner.nextInt();
        System.out.println("Ingrese el segundo numero ");
        num2=scanner.nextInt();
        salida = (num1>num2)?num1:num2;
        System.out.println("El numero mayor es: "+salida);    
    }
    
}
