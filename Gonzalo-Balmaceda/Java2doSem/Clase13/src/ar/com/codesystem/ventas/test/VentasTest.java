package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);

        Orden orden1 = new Orden();
        // Agregamos productos al arreglo.
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();

        // Tarea:
        // Crear más objetos de tipo 'Producto' al menos 10.
        // Crear más objetos de tipo 'Orden' al menos 2.

        Producto prenda1 = new Producto("Remera Oversize", 12000.00);
        Producto prenda2 = new Producto("Remera Térmica", 15000.00);
        Producto prenda3 = new Producto("Musculosa", 5000.00);
        Producto prenda4 = new Producto("Buzo", 17500.00);
        Producto prenda5 = new Producto("Rompe Viento", 20000.00);

        Orden prendasSuperiores = new Orden();
        prendasSuperiores.agregarProducto(prenda1);
        prendasSuperiores.agregarProducto(prenda2);
        prendasSuperiores.agregarProducto(prenda3);
        prendasSuperiores.agregarProducto(prenda4);
        prendasSuperiores.agregarProducto(prenda5);

        System.out.println();
        prendasSuperiores.mostrarOrden();

        Producto prenda6 = new Producto("Short", 5500.00);
        Producto prenda7 = new Producto("Pantalon Cargo", 20000.00);
        Producto prenda8 = new Producto("Malla", 7500.00);
        Producto prenda9 = new Producto("Jeans", 25000.00);
        Producto prenda10 = new Producto("Zapatilla Deportiva", 50000.00);

        Orden prendasInferiores = new Orden();
        prendasInferiores.agregarProducto(prenda6);
        prendasInferiores.agregarProducto(prenda7);
        prendasInferiores.agregarProducto(prenda8);
        prendasInferiores.agregarProducto(prenda9);
        prendasInferiores.agregarProducto(prenda10);

        System.out.println();
        prendasInferiores.mostrarOrden();
    }
}
