package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {

    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon: ", 9500.00);
        Producto producto2 = new Producto("Campera: ", 29500.00);

        Orden orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();

        //Tarea
        //Crear mas objetos de tipo Productos = 10
        //Crear mas objetos de tipo orden = 2
        Producto productoK = new Producto("Gorra", 2000.00);
        Producto productoL = new Producto("Zapatillas", 15000.00);
        Producto productoM = new Producto("Cinturon", 3000.00);
        Producto productoN = new Producto("Gafas de sol", 5000.00);
        Producto productoO = new Producto("Sombrero", 7000.00);
        Producto productoP = new Producto("Calcetines", 1500.00);
        Producto productoQ = new Producto("Shorts", 6000.00);
        Producto productoR = new Producto("Collar", 4500.00);
        Producto productoS = new Producto("Reloj", 10000.00);
        Producto productoT = new Producto("Chaqueta", 18000.00);

        Orden orden2 = new Orden();
        orden2.agregarProducto(productoK);
        orden2.agregarProducto(productoL);
        orden2.mostrarOrden();

        Orden orden3 = new Orden();
        orden3.agregarProducto(productoM);
        orden3.agregarProducto(productoN);
        orden3.agregarProducto(productoO);
        orden3.mostrarOrden();
    }
}
