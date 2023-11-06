
package Caja;

public class Caja {
    int ancho;
    int alto;
    int profundo;
    public Caja(){
    }
    public Caja(int ancho, int alto, int profundo){
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    public int calcularVolumen(){
        return ancho * alto * profundo;
    }
}
