package PasoPorValor;

public class PasoPorValor {
    public static void main(String[] args) {

        // POO: Paso por valor.
        int numeroX = 20;
        cambioValor(numeroX); // Hacemos una copia.
        System.out.println("numeroX = " + numeroX);
    }
    public static void cambioValor(int arg1) {
        System.out.println("arg1 = " + arg1); // Mostramos la copia.
    }
}
