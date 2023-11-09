package domain;

public class Empleado extends Persona {
    protected int idEmpleado;
    protected double sueldo;
    protected static int contadorEmpleado; // Es para incrementar

    // constructores.
    public Empleado() { // Constructor 1
        this.idEmpleado = ++Empleado.contadorEmpleado;
    }

    public Empleado(String nombre, double sueldo) { // Constructor 2
        //super(nombre); // Lo comentamos porque no se puede usar el super() y el this().
        this(); // Llamamos al constructor vació (Llamar al constructor interno).
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    // Setters y Getters.
    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Empleado {");
        sb.append("idEmpleado= ").append(idEmpleado);
        sb.append(", sueldo= ").append(sueldo);
        sb.append(", ").append(super.toString()); // Traemos el toString() de la clase 'Persona'.
        sb.append('}');
        return sb.toString();
    }
}
