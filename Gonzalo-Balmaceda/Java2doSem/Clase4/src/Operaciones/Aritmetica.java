package Operaciones;

public class Aritmetica {
    // Atributos de la Clase
    int a;
    int b;

    // El constructor es un método especial.
    public Aritmetica() {
        System.out.println("Ejecutando constructor uno");
    }

    // Estamos viendo lo que se llama sobre carga de constructores.
    public Aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el costructor dos");
    }
    // Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    public int sumarConRetorno() {
        return (a + b);
    }

    public int sumarConArgumentos(int a, int b) {
        this.a = a; // El argumento a se le asigna al atributo this.a
        this.b = b;
        //return (a + b);
        return sumarConRetorno();
    }
}
