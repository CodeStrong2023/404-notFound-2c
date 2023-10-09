package PasoPorValor;

public class PasoPorValor {
    public static void main(String[] args) {
       var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); // Solo le enviamos una copia, por que está copiando el valor recibido en la variable local
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg1){ // Parámetros por valor
        System.out.println("arg1 = " + arg1);
        arg1 = 15;
    }
    
}
