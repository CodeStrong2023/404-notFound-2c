package test;

import domain.Cliente;
import domain.Empleado;
import domain.Persona;

import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Gonzalo", 57000.00);
        // Muestra el toString() de la clase Empleado y dentro el toString() que llamamos de la clase Persona.
        System.out.println("empleado1 = " + empleado1);

//        Cliente cliente1 = new Cliente(new Date(), true, "Gonzalo", 'M', 20, "Avellaneda 2626");
//        System.out.println("cliente1 = " + cliente1);

//        Cliente cliente2 = new Cliente(new Date(), false, "Nicolas", 'M', 20, "San Pedro");
//        System.out.println("cliente2 = " + cliente2.getIdCliente());
    }
}
