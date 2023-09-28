package Operaciones;

public class Aritmética {
    // Atributos de la clase
    int a;
    int b;
    
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
    public int sumarConArgumentos(int a, int b){
        this.a = a; // El argumento a se asigna el atributo this.a
        this.b = b; // No modifica los valores delos atraibutos del objeto.
        //return a + b; // Retorno de la suma.
        return this.sumaConRetorno(); // El operador this hace que se diferencien los atributos de los argumentos, aunque tengan el mismo nombre.
    }
    // Parámetro y argumento son lo mismo, es lo que se envía y lo que se recibe
    // Operador this: sirve también para tener un código más legible.
    
}
