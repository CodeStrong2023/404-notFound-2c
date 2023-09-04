
package CicloWhile;


public class EjercicioWhile01 {
    public static void main(String[] args) {
       //Ejemplo Ciclo While
        var conteo = 0; //Inferencia de tipos
        while (conteo <3){
            System.out.println("conteo = " + conteo);
            conteo ++; //vamos aumentando en 1 la variable
        }
        //Ejemplo Ciclo Do While
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador ++;
        }while(contador <7);
        
        //Ejemplo Ciclo For
        for(var contando = 0; contando < 7; contando ++){
            System.out.println("contando = " + contando);
        }
        inicio:
        for(var contando = 0; contando < 7; contando ++){
            if(contando % 2 == 0){
            System.out.println("contando = " + contando); 
            break;
            } 
        }
        for(var contando = 0; contando < 7; contando ++){
            if(contando % 2 != 0){
                continue; //vamos a la siguiente iteracion  
            } 
            System.out.println("contando = " + contando);
        }
        
        // Uso de las palabras break y continue con las etiquetas (Labels)
       
        for(var contando = 0; contando < 7; contando ++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break ;
        
            } 
        }
        inicio:
        for(var contando = 0; contando < 7; contando ++){
            if(contando % 2 != 0){
                continue inicio;
            }
            System.out.println("contando = " + contando);
        }
        
    }
}
