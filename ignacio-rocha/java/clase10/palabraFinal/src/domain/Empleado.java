package domain;

public class Empleado  extends Persona {
    @Override
    public void imprimir(){
        System.out.println("metodo imprimir desde la clase hija");
    }
}
