package test;

import operaciones.Operaciones;

public class TestOperaciones {
    public static void main(String[] args) {
        var resultado = Operaciones.sumar(5, 10);
        System.out.println("operaciones = " + resultado);

        var resultado2 = Operaciones.sumar(5.5, 9.5);
        System.out.println("resultado2 = " + resultado2);
    }
}
