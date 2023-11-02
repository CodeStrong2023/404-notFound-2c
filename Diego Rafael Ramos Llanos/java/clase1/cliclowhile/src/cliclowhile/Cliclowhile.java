
package cliclowhile; 
public class Cliclowhile {
    public static void main(String[] args) {
        var numer = 0;
        while (numer<7){
        System.out.println("numer = " + numer);
        numer++;
        }
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador<=7);
        inicio:
        for( var contando=0;contando<7 ;contando++ ){
            if (contando%2==0){
            System.out.println("contando = " + contando);
            break inicio;
            }
        }inicio:
         for( var contando=0;contando<7 ;contando++ ){
            if (contando%2!=0){
            continue inicio;
            }
            System.out.println("contando = " + contando);
        }
    }
    
}
