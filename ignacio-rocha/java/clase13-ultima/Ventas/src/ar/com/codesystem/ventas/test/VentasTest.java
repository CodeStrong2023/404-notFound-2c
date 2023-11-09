package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.Orden;
import ar.com.codesystem.ventas.Producto;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1=new Producto("Pantalon",9500.00);
        Producto producto2=new Producto("campera",29900.00);
       

        //tarea:
        //crear mas objetos de tipo Producto -10
        Producto producto3=new Producto("zapato",19900.00);
        Producto producto4=new Producto("gorra",9900.00);
        Producto producto5=new Producto("medias",9900.00);
        Producto producto6=new Producto("remera",39900.00);
        Producto producto7=new Producto("guantes",8900.00);
        Producto producto8=new Producto("sweter",59900.00);
        Producto producto9=new Producto("musculosa",79900.00);
        Producto producto10=new Producto("pantalon de verano",39900.00);
        Producto producto11=new Producto("rodilleras",29900.00);
        Producto producto12=new Producto("visera",29900.00);
        //crear mas objetos de tipo orden - 2
        Orden orden1=new Orden();
        //agregamos  productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.mostrarOrden();
        
        
    }
}
