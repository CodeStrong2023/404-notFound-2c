package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; // Variables locales
        int b = 7;  // Memoria STACK
        miMetodo(); // Los atributos no son lo mismo que una variable, tienen un alcance superior a una variable local(a través de new).
        Aritmética aritmetica1 = new Aritmética();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        // Para almacenar un objeto o los atributos se utiliza la memoria Heap.
        int resultado = aritmetica1.sumaConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmética1 a: "+aritmetica1.a);
        System.out.println("aritmética1 b: "+aritmetica1.b);
        
        Aritmética aritmética2 = new Aritmética(5, 8);
        System.out.println("aritmética2 = " + aritmética2.a);
        System.out.println("aritmética2 = " + aritmética2.b);
        // aritmetica1 = null; nunca utilizar esto
        // System.gc(); //GARBAGE COLECTOR, recolector de basura. Para limpiar residuos, muy pesado no utilizar 
        Persona persona = new Persona("Enzo", "Astorga");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }
    
    // Modularidad: Creamos un nuevo método
    public static void miMetodo(){
        ///int a = 10; // Una variable está limitada
        System.out.println("Aquí hay otro método");
    }
    
}

// Creamos una nueva clase
class Persona{
    String nombre; // Atributos
    String apellido;
    
    Persona(String nombre, String apellido){ // Constructor que apunta hacia los atributos
        super(); // Llamada al constructor de la clase Padre OBJECT
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){ // Método Constructor
        super(); // El constructor de la clase padre, para reservar la memoria.
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
     // EL USO DE LA PALABRA THIS ES APUNTAR AL OBJETO Y CAMBIAR SEGÚN EL OBJETO QUE SE ESTÁ EJECUTANDO.        
}