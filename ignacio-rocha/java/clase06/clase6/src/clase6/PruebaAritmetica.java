package clase6;


public class PruebaAritmetica {
    public static void main(String[] args) {
        int a=10; //variables locales
        int b=7; //memoria stack
        miMetodo();//llamamos el metodo nuevo
        Aritmetica aritmetica1=new Aritmetica();
        aritmetica1.a=3;
        aritmetica1.b=7;
        
        aritmetica1.sumarNumeros();
        //para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado=aritmetica1.sumarConRetorno();
        System.out.println("resultado = "+resultado);
        
        resultado=aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = "+resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        
        Aritmetica aritmetica2= new Aritmetica(5,8);
        System.out.println("Aritmetica2="+aritmetica2.a);
        System.out.println("Aritmetica2="+aritmetica2.b);
        //aritmetica1=null; no usar
        //System.gc(); metodo para limipiar residuos
       
    
    }
    public static void miMetodo(){
        //int a=10;//una variable esta limitada
        System.out.println("aqui hay otro metodo");
    }
}

