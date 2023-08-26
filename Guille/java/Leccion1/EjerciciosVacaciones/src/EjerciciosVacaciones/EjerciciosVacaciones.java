
package EjerciciosVacaciones;

import java.util.Scanner;

public class EjerciciosVacaciones {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        //Ejercicio 1: Ingresar 3 calificaciones, sacar promedio y decir si el alumno esta aprobado o no
        
        System.out.println("Ingrese la calificaciones 1: ");
        var calificacion1 = Float.parseFloat(entrada.nextLine());

        System.out.println("Ingrese la calificacion 2: ");
        var calificacion2 = Float.parseFloat(entrada.nextLine());
        
        System.out.println("Ingrese la calificacion 3: ");
        var calificacion3 = Float.parseFloat(entrada.nextLine());
        
        var promedio = (calificacion1 + calificacion2 + calificacion3)/3;
        
        if (promedio >= 7){
            System.out.println("El alumno esta aprobado con: "+ promedio);
        }
        else {
            System.out.println("El alumno esta desaprobado con: " + promedio);
            
        }
        
        //Ejercicio 2: Descuento de almacen del 20% cuando la compra supere los $100
        
        System.out.println("Ingrese el monto a pagar: ");
        var compra = Float.parseFloat(entrada.nextLine());
        
        if (compra > 100) {
            var descuento = compra * 0.20;
            var precioFinal = compra - descuento;
            System.out.println("El monto a pagar es: " + precioFinal);
            }else {
            System.out.println("El monto a pagar es: "+ compra );
        }
        
        //Ejercicio 3: leer 2 num, si son iguales que los multiplique, si el primero el mayor que el segundo que los reste
        //y si no que los sume
        
        System.out.println("Ingrese el primer numero: ");
        var num1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el segundo numero: ");
        var num2 = Integer.parseInt(entrada.nextLine());
        
        if (num1 == num2){
            var resultado = num1*num2;
            System.out.println("El resultado es: "+ resultado);
            }
        else if (num1 > num2) {
            var resultado = num1 - num2;
            System.out.println("El resultado es: "+ resultado);
        }else {
                var resultado = num1 + num2;
                System.out.println("El resultado es: "+ resultado);
                }
        
    }
    
}
