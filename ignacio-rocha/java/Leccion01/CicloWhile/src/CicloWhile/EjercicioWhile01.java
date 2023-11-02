package CicloWhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        int conteo=0; //inferencia de tipos
        while(conteo<7){
            System.out.println("conteo = "+conteo);
            conteo++;//vamos aumentando en uno la variable
        }
        
        int  contador=5;
        do{
            System.out.println("contador="+contador);
            contador++;
        }while (contador<=7);
        
        //uso de las palabras break y continue junto a las etiquetas (labels)
        inicio:
         for(int contando=0;contando<7;contando++){
            if (contando!=0){
                continue;//vamos a la siguiente iteracion
            }
            System.out.println("contando="+contando);
         
            if(contando%2==0){
                 System.out.println("contando = "+contando);
                 break inicio;
            }
           
        }
        //etiquetas labels
        for(int contando=0;contando<7;contando++){
            if (contando!=0){
                continue;//vamos a la siguiente iteracion
            }
            System.out.println("contando="+contando);
         
            /*if(contando%2==0){
                 System.out.println("contando = "+contando);
                 break;
            }*/
           
        }
        
        
        
    }
}
