
package javaclase06;


public class PruebaAritmética {
    public static void main(String[] args) {
        int a = 10; //Variables locales
        int b = 7; //Memoria stack
        miMetodo(); //Llamamos el método nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resiltado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmética1 a: "+aritmetica1.a);
        System.out.println("aritmética1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmética2 1: "+aritmetica2.a);
        System.out.println("aritmética2 b: "+aritmetica2.b);
        //aritmetica1 = null; nunca utilizar esto, no se debe hacer
        //System.gc(); método para limpiar residuos, es pesado, no utilizar
    }
    
    public static void miMetodo(){
        int a = 10;
        System.out.println("Aquí hay otro método");
    }
            
}
