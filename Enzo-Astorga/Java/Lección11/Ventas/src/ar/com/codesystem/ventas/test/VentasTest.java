package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalón", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3=new Producto("Medias", 1300.00);
        Producto producto4=new Producto("Remera", 7999.00);
        Producto producto5=new Producto("Mayas", 5500.00);
        Producto producto6=new Producto("Remera manga larga", 8000.00);
        Producto producto7=new Producto("Buzo con capucha", 12000.00);
        Producto producto8=new Producto("Buzo cuello redondo", 9000.00);
        Producto producto9=new Producto("Gorra", 5500.00);
        Producto producto10=new Producto("Gorro de lana", 4500.00);
        Producto producto11=new Producto("Cuellito", 4000.00);
        Producto producto12=new Producto("Boxer", 1900.00);
        
        Orden orden1 = new Orden();
        // Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        orden1.agregarProducto(producto6);
        orden1.agregarProducto(producto7);
        orden1.agregarProducto(producto8);
        orden1.agregarProducto(producto9);
        orden1.agregarProducto(producto10);
        orden1.agregarProducto(producto11);
        orden1.agregarProducto(producto12);
        orden1.mostrarOrden();
        
        // Tarea:
        // Crear más objetos de tipo Producto = 10
        // Crear más objetos de tipo Orden = 2
    }
    
}
