package leccion6;

public class aritmetica {
    //Atributos de la clase

    int a;
    int b;

    public aritmetica() {//constructor 1 vacio
        System.out.println("Se esta ejecutando este constructor numero uno--");
    }

    //estamos viendo lo que se llama sobrecarga de constructores
    public aritmetica(int a, int b) { //constructor 2
        this.a = a;
        this.b = b;
        System.out.println("se esta ejecutando este constructor numero dos--");
    }

    public void SumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    public int sumaretorno() {
        //int resultado = a+b;
        return a + b;
    }

    public int sumarConArgumentos(int arg1, int arg2) {
        this.a = arg1;
        this.b = arg2; // No modifica los valores de los atraibutos del objeto.
        //return a + b; 
        return this.sumaretorno();
    }
}
