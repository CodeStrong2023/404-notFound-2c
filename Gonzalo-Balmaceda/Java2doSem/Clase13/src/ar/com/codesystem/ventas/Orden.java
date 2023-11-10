package ar.com.codesystem.ventas;

public class Orden {
    private int idOrden;
    private Producto productos[]; // Declaramos el array.
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;

    // Constructor Vacío.
    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[MAX_PRODUCTOS]; // Le asignamos un limite máximo al array.
    }

    // Métodos
    public void agregarProducto(Producto producto) {
        if (this.contadorProductos < Orden.MAX_PRODUCTOS) {
            this.productos[this.contadorProductos++] = producto;
        } else {
            System.out.println("Se ha superado el máximo de productos: " + Orden.MAX_PRODUCTOS);
        }
    }

    public double calcularTotal() {
        double total = 0; // Variable temporal
        for (int i = 0; i < this.contadorProductos; i++) {
            total += this.productos[i].getPrecio(); // Iteramos cada posición del array y sumamos los precios de los productos.
        }
        return total;
    }

    public void mostrarOrden() {
        System.out.println("id de la orden: " + idOrden);
        double totalOrden = this.calcularTotal();
        System.out.println("El total de la orden es: $" + totalOrden);
        System.out.println("Productos de la orden: ");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);
        }
    }
}
