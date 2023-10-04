
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
        Persona persona = new Persona("Guillermo","Giannone");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }
    // Modularidad creamos un nuevo metodo
    public static void miMetodo(){
        //a = 10; //Una variable esta limitada
        System.out.println("Aqui hay otro metodo");
    }   
}
// Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ // Constructor
        super();//Llamada al constructor de la clase Padre Object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().Imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){
        super();//el constructor de la clase padre, para reservar memoria
    }
    public void Imprimir(Persona persona){
        System.out.println("Persona desde la clase Imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }
}
