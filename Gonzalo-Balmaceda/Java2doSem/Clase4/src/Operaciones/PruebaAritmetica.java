package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {

        // Creamos variables locales.
        int a = 10;  // Las variables locales trabajan con la memoria stack
        int b = 5;
        miMetodo(); // Llamamos al método.

        // Para almacenar un objeto o los atributos se utiliza la memoria heap
        Aritmetica num1 = new Aritmetica();

        // Usamos los atributos de la clase que creamos.
        num1.a = 10;
        num1.b = 15;

        // Utilizamos el método sumarNumeros().
        num1.sumarNumeros();

        // Utilizamos wl método sumarConRetorno().
        int resultado = num1.sumarConRetorno();
        System.out.println("resultado con retorno = " + resultado);

        // Utilizamos el método sumarConArgumentos();
        resultado = num1.sumarConArgumentos(10, 5);
        System.out.println("resultado usando argumentos = " + resultado);

        System.out.println("num1.a = " + num1.a);
        System.out.println("num1.b = " + num1.b );

        // Creamos un nuevo objeto que va a trabajar con el segundo constructor.
        Aritmetica constructor2 = new Aritmetica(5, 8);
        System.out.println("constructor2 = " + constructor2.a);
        System.out.println("constructor2 = " + constructor2.b);

        // Usamos la nueva clase Persona creada.
        Persona persona = new Persona("Gonzalo", "Balmaceda");
        System.out.println("persona = " + persona);
        System.out.println("persona nombre = " + persona.nombre);
        System.out.println("persona apellido = " + persona.apellido);
    }

    // Modularidad, creamos un nuevo método.
    public static void miMetodo() {
//        int a = 10; Una variable esta limitada
        System.out.println("Aqui hay otro método");
    }
}
// Creamos una nueva clase.
class Persona {
    String nombre;
    String apellido;

    Persona(String nombre, String apellido) { // Constructor.
        super(); // Llmada al constructor de la clase padre Object.
        // Imprimir imprimir = new imprimir();
        new imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this = " + this);
    }

    class imprimir {
        public imprimir() {
            super(); // El constructor de la clase padre para reservar memoria.
        }

        public void imprimir(Persona persona) {
            System.out.println("Persona desde la clase impirmir = " + persona);
            System.out.println("Impresion del objeto actual = " + this);
        }
    }
}
