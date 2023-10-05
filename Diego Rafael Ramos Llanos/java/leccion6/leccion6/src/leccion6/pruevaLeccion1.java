/*Proyecto caja:
Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
La formula es: volumen = ancho * alto * profundidad*/
package leccion6;

public class pruevaLeccion1 {
        public static void main(String[] args) {
        ejercicio1 miCaja = new ejercicio1(3, 2, 6);
        double volumen1 = miCaja.calcularVolumen();
        System.out.println("El volumen de la caja es: " + volumen1);
        
        ejercicio1 miCaja2 = new ejercicio1(2, 4, 6);
        double volumen2 = miCaja2.calcularVolumen();
        System.out.println("El volumen de la cja 2 es: "+volumen2);
    }
    
}
