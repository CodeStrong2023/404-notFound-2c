/*Proyecto caja:
Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
La formula es: volumen = ancho * alto * profundidad*/
package leccion6;

public class ejercicio1 {
    // Propiedades de la caja y ademas el private es para para que no puedan ser modificadas en un futuro desde fuera
    private double ancho;
    private double alto;
    private double profundidad;

    // Constructor
    public ejercicio1(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    // Método para calcular el volumen de la caja
    public double calcularVolumen() {
        return ancho * alto * profundidad;
    }

}
