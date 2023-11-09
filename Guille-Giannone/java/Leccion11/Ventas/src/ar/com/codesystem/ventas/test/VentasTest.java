
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;



public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon Jeans", 9500.00);
        Producto producto2 = new Producto("Campera", 29500.00);
        Producto producto3 = new Producto("Remera", 5200.00);
        Producto producto4 = new Producto("Medias", 1300.00);
        Producto producto5 = new Producto("Buzo", 12000.00);
        Producto producto6 = new Producto("Sueter", 10000.00);
        Producto producto7 = new Producto("Bufanda", 2500.00);
        Producto producto8 = new Producto("Guantes", 4000.00);
        Producto producto9 = new Producto("Bermudas", 7800.00);
        Producto producto10 = new Producto("Pantalon Deportivo", 8500.00);
        
        
      Orden orden1 = new Orden();
      orden1.agregarProducto(producto1);
      orden1.agregarProducto(producto2);
      orden1.mostrarOrden();
      
      Orden orden2 = new Orden();
      orden2.agregarProducto(producto4);
      orden2.agregarProducto(producto6);
      orden2.agregarProducto(producto9);
      orden2.mostrarOrden();
      
      Orden orden3 = new Orden();
      orden3.agregarProducto(producto10);
      orden3.agregarProducto(producto7);
      orden3.agregarProducto(producto3);
      orden3.agregarProducto(producto8);
      orden3.mostrarOrden();
      
      Orden orden4 = new Orden();
      orden4.agregarProducto(producto5);
      orden4.mostrarOrden();
      //Tarea
      //Crear mas objetos de tipo Productos = 10
      //Crear mas objetos de tipo orden = 2
    }
}
