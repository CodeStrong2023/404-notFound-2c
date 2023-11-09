package caja;

public class Caja {
    int ancho;
    int alto;
    int profundo;

    public Caja() {

    }

    // Caja con parametros.
    public Caja(int ancho, int alto, int profundo) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }

    // Método para calcular la caja.
    public int calcularCaja() {
        return (ancho * alto * profundo);
    }
}
