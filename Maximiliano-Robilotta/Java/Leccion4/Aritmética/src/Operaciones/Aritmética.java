package Operaciones;

public class Aritmética {
    // Atributos de la clase
    int a;
    int b;
    
    /* El constructor es un método especial, tiene 3 objetivos:
    Construye un objeto
    Reserva un espacio de memoria
    Inicializa los atributos de la clase
    */
    public Aritmética(){ // Constructor 1(vacío)
        System.out.println("Se está ejecutando este constructor número 1.");
    }
    // Estamos viendo lo que se llama sobrecarga de constructores.
    public Aritmética(int a, int b){ // Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando este constructor número 2.");
        
    }
    
    //Método
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumaConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }
    // public: modificador de acceso. Int o void: Tipo de retorno que va a tener el método, en este caso de tipo entero.
    // sumarConArgumentos: Identificador del método o nombre.
    // int arg1, int arg2: Argumento, es la información que va a recibir el método.
    public int sumarConArgumentos(int a, int b){  // Inferencia de tipo no se utiliza en argumentos o parámetros(var)
        this.a = a; // El argumento a se asigna el atributo this.a
        this.b = b; // No modifica los valores delos atraibutos del objeto.
        //return a + b; // Retorno de la suma.
        return this.sumaConRetorno(); // El operador this hace que se diferencien los atributos de los argumentos, aunque tengan el mismo nombre.
    }
    // Parámetro y argumento son lo mismo, es lo que se envía y lo que se recibe
    // Operador this: sirve también para tener un código más legible.
    
    /* ENGINEER JAVA: MEMORIA STACK Y HEAP. Tratamiento de residuos
    Stack y heap son clasificaciones de la memoria, el Stack tiene que ver con las variables locales y solo almacena la referencia del objeto.
    Al crear atributos y objetos utilizan la memoria HEAP
    */
}
