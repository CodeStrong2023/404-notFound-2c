package clase07;

public class AritmeticaClase07 {
   
        //Atributos de clase
        int a;
        int b;
        
        //el constructor es un metodo especial
        public AritmeticaClase07(){//constructor 1 vacio
            System.out.println("Se esta ejecutando este constructor numero uno");
        }
        
        //estamos viendo lo que se llama sobrecarga de constructores
        public AritmeticaClase07(int a,int b){ //constructor 2
            this.a=a;
            this.b=b;
            System.out.println("se esta ejecutando este constructor numero dos");
        }
        //metodo
        public void sumarNumeros(){
            int resultado=a+b;
            System.out.println("resultado = " + resultado);
        }
        
        public int sumarConRetorno(){
            //int resultado=a+b;
            return a+b;
        }
        public int sumarConArgumentos(int a, int b){
            this.a=a; //el argumento a se asigna al atributo this.a
            this.b=b;
            //return a+b;
            return this.sumarConRetorno();
        }
        
        
    }

