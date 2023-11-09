package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        Caja caja1 = new Caja();
        caja1.alto = 2;
        caja1.ancho = 2;
        caja1.profundo = 5;

        int volumenCaja1 = caja1.calcularCaja();
        System.out.println("El volumen de la caja1 es = " + volumenCaja1);

        // Prueba de caja con parámetros.

        Caja caja2 = new Caja(2, 2, 3);
        System.out.println("El volumen de la caja2 es = " + caja2.calcularCaja());
    }

}
