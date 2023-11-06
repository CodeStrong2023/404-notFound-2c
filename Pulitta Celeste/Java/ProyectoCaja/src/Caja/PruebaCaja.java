/*
Proyecto caja: 
Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
La formula es: volumen = ancho * alto * profundidad
*/
package Caja;

public class PruebaCaja {
    public static void main(String[] args) {
        int medidaAncho = 5;
        int medidaAlto = 3;
        int medidaProfundidad = 9;
        
        Caja caja1 = new Caja();
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProfundidad;
        int resultado = caja1.calcularVolumen();
        System.out.println("Resultado del volumen de caja1 es: "+resultado);
        
        Caja caja2 = new Caja(3, 2, 6);
        System.out.println("Resultado del volumen de caja2: "+caja2.calcularVolumen());
    }
}
