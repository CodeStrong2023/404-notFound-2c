package test;

import java.util.Date;
import domain.Empleado;
import domain.Cliente;
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1=new Empleado("ariel",57000.0);
        System.out.println("empleado1= "+empleado1);
        Cliente cliente1=new Cliente(new Date(),true,"bety",'F',32,"9 de julio de 1413");
        System.out.println("cliente1 = " + cliente1);
        
    }
}
