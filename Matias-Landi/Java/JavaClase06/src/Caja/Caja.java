
/*
Proyecto caja:
Ejercicio 1: Crear un proyecto según las especificaciones mostradas a
continuación.
La fórmula es: volúmen = ancho * alto * profundidad
 */
 
package Caja;


public class Caja { //Clase pública caja
    //Atributos (Características)
    int ancho;
    int alto;
    int profundo;
    //Métodos y constructores (acciones)
    public Caja() {
        
    }
    //Constructor con parámetros
    public Caja(int ancho, int alto, int profundo) { //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen() {
        return ancho * alto * profundo;
    }
    
}
