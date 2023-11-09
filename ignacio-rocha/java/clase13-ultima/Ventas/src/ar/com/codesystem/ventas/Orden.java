package ar.com.codesystem.ventas;

public class Orden {

    private int idOrden;
    private Producto productos[];//declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;

    //constructor vacio
    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }

    public void agregarProducto(Producto producto) {
        if (this.contadorProductos < Orden.MAX_PRODUCTOS) {
            this.productos[contadorProductos++] = producto;
        } else {
            System.out.println("se ha superado el maximo de productos: " + Orden.MAX_PRODUCTOS);

        }
    }
    public double calcularTotal(){
        double total=0;//variable temporal
        for (int i = 0; i < contadorProductos; i++) {
            //Producto producto = this.productos[i];
            //total+=producto.getPrecio();
            total+=this.productos[i].getPrecio();
        }
        return total;
        
    }
    public void mostrarOrden(){
        System.out.println("id orden: "+idOrden);
        double totalOrden=this.calcularTotal();
        System.out.println("el caso de la orden es:$"+totalOrden);
        System.out.println("productos de la orden:");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i].getNombre());
            
        }
        
    }

}
