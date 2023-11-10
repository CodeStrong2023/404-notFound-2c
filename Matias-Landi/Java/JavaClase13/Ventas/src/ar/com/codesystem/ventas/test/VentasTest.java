
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;



public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalón", 9500.00);
        Producto producto2 = new Producto("Campera", 29500.00);
        Producto producto3 = new Producto("Remera", 4500.00);
        Producto producto4 = new Producto("Medias", 1000.00);
        Producto producto5 = new Producto("Boxers", 2000.00);
        Producto producto6 = new Producto("Zapatillas", 80000.00);
        Producto producto7 = new Producto("Buzo", 25000.00);
        Producto producto8 = new Producto("Malla", 10000.00);
        Producto producto9 = new Producto("Crocs", 18000.00);
        Producto producto10 = new Producto("Muñequera", 1800.00);
        
        
      Orden orden1 = new Orden();
      orden1.agregarProducto(producto1);
      orden1.agregarProducto(producto2);
      orden1.mostrarOrden();
      
      Orden orden2 = new Orden();
      orden2.agregarProducto(producto1);
      orden2.agregarProducto(producto1);
      orden2.agregarProducto(producto7);
      orden2.mostrarOrden();
      
      Orden orden3 = new Orden();
      orden3.agregarProducto(producto10);
      orden3.agregarProducto(producto5);
      orden3.agregarProducto(producto3);
      orden3.agregarProducto(producto2);
      orden3.mostrarOrden();
      
      Orden orden4 = new Orden();
      orden4.agregarProducto(producto5);
      orden4.mostrarOrden();
      //Tarea
      //Crear mas objetos de tipo Productos = 10
      //Crear mas objetos de tipo orden = 2
    }
}
