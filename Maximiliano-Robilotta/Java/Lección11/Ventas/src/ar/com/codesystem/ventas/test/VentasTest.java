package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalón", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3=new Producto("Cuello", 1300.00);
        Producto producto4=new Producto("Calzoncillo", 999.00);
        Producto producto5=new Producto("Pantalon corto", 4500.00);
        Producto producto6=new Producto("Musculosa", 8000.00);
        Producto producto7=new Producto("Medias", 1200.00);
        Producto producto8=new Producto("Bermuda", 5000.00);
        Producto producto9=new Producto("Remera", 6000.00);
        Producto producto10=new Producto("Bufanda", 2500.00);
        Producto producto11=new Producto("Calzones", 2000.00);
        Producto producto12=new Producto("Buzos", 19900.00);
        
        Orden orden1 = new Orden();
        // Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.mostrarOrden();
        
        // Tarea:
        // Crear más objetos de tipo Producto = 10
        // Crear más objetos de tipo Orden = 2
    }
    
}
