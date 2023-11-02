package proyectoCaja;

public class PruebaCaja {
    public static void main(String[] args) {//metodo main
        //variables locales
        int medidaAncho=3; //valores ingresados en codigo duro
        int medidaAlto=2;
        int medidaProf=6;
        
        Caja caja1=new Caja(); //instanciamos el objeto, constructor vacio
        caja1.ancho=medidaAncho;//le pasamos los valores al objeto
        caja1.alto=medidaAlto;
        caja1.profundo=medidaProf;
        int resultado=caja1.calcularVolumen(); //llamamos al metodo
                
        //primer resultado
        System.out.println("resultado volumen de caja 1: "+resultado);
        
        Caja caja2=new Caja(2,4,6); //llamamos al constructor 2 con nuevos argumentos
        //llamamos con el nnuevo objeto al metodo para un nuevo calculo
        System.out.println("resultado volumen de caja 2: "+caja2.calcularVolumen());
              
    }
}
