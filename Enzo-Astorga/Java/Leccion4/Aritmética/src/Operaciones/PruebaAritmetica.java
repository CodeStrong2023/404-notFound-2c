package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmética aritmetica1 = new Aritmética();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumaConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
    }
    
}
