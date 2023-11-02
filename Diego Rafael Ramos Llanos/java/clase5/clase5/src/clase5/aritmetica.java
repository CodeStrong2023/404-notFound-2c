
package clase5;

public class aritmetica {
        //Atributos de la clase
    int a;
    int b;
    public void SumarNumeros(){
    int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    public int sumaretorno(){
        //int resultado = a+b;
        return a+b;
    }
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1;
        this.b = arg2; // No modifica los valores de los atraibutos del objeto.
        //return a + b; 
        return this.sumaretorno();
    }
}
