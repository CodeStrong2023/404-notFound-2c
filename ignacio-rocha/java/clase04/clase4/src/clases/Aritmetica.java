package clases;

public class Aritmetica {
   
        //Atributos de clase
        int a;
        int b;
        
        //metodo
        public void sumarNumeros(){
            int resultado=a+b;
            System.out.println("resultado = " + resultado);
        }
        
        public int sumarConRetorno(){
            //int resultado=a+b;
            return a+b;
        }
        public int sumarConArgumentos(int arg1, int arg2){
            this.a=a; //el argumento a se asigna al atributo this.a
            this.b=b;
            //return a+b;
            return this.sumarConRetorno();
        }
        
        
    }

