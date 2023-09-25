
package Operaciones;


public class PruebasAritmeticas {
    public static void main(String[] args) {
        var a = 10; //variables locales
        int b = 7; //Memoria stack
        miMetodo();//Llamamos al metodo nuevo
        
        
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        //Para almacenar un objeto a los atributos se utiliza la memoria HEAP
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12 , 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("Aritmetica1 a:"+aritmetica1.a);
        System.out.println("Aritmetica1 b:"+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null; Nunca utilizar esto no se debe hacer
        //System.gc(); Metodo para limpiar residuos, muy pesado no utilizar
        
    }
    
    public static void miMetodo(){
        //a = 10; //Una variable esta limitada
        System.out.println("Aqui hay otro metodo");
    }
    
}