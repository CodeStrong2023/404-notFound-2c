
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    // El contructor es un método especial
    public Aritmetica(){//Constructor 1 
        System.out.println("Se esta ejecutando el contructor número uno");
    }
    //Estamos viendo lo que se llama sobre carga de constructores
    public Aritmetica(int a, int b){//Constructor dos
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el contructor número dos");
    }
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    public int sumarConArgumentos(int a, int b){
        this.a = a;// El argumento a se asigna al atributo this.a
        this.b = a;
        //return a + b;
        return this.sumarConRetorno();
        
    }
}
