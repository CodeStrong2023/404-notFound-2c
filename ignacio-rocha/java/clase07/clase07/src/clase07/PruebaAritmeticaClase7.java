package clase07;

public class PruebaAritmeticaClase7 {

    public static void main(String[] args) {
        int a = 10; //variables locales
        int b = 7; //memoria stack
        miMetodo();//llamamos el metodo nuevo
        AritmeticaClase07 aritmetica1 = new AritmeticaClase07();
        aritmetica1.a = 3;
        aritmetica1.b = 7;

        aritmetica1.sumarNumeros();
        //para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);

        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);
        AritmeticaClase07 aritmetica2 = new AritmeticaClase07(5, 8);
        System.out.println("Aritmetica2=" + aritmetica2.a);
        System.out.println("Aritmetica2=" + aritmetica2.b);
        //aritmetica1=null; no usar
        //System.gc(); metodo para limipiar residuos
               Persona persona = new Persona("ariel", "betancud");
        System.out.println("persona = " + persona);
        System.out.println("persona nombre: " + persona.nombre);
        System.out.println("persona apellido: " + persona.apellido);

    }

    //modularidad creamos un nuevo metodo 
    public static void miMetodo() {
        //int a=10;//una variable esta limitada
        System.out.println("aqui hay otro metodo");
    }
}


//creamos una nueva clase
class Persona {

        String nombre;
        String apellido;

        Persona(String nombre, String apellido) {//constructor
            
            super();//llamada al constructor de la clase padre object
            //Imprimir imprimir =new Imprimir();
            new Imprimir().imprimir(this);
            this.nombre = nombre;
            this.apellido = apellido;
            System.out.println("objeto persona usando this: "+this);
        }
    }
 
class Imprimir {

    public Imprimir() {
        super();//el constructor de la clase padre, para reservar memoria
    }
    public void imprimir(Persona persona){
        System.out.println("persona desde la clase imprimir "+persona);
        System.out.println("impresion del objeto actual (this) :"+this);
        
    }
}
