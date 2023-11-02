
package clase5;

public class pruevaAritmetica {
    public static void main(String[] args) {
        aritmetica aritmetica1=new aritmetica();
        aritmetica1.a=3;
        aritmetica1.b=7;
        aritmetica1.SumarNumeros();
        int resultado = aritmetica1.sumaretorno();
        System.out.println("resultado= " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
    }
    
}
