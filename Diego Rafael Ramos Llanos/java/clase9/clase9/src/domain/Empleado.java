package domain;

public class Empleado extends Persona {
    protected int idEmpleado;
    protected double sueldo;
    protected static int contadorEmpleado; // incrementar

    // construc.
    public Empleado(String nombre, double sueldo) {
        super(nombre);
        this.idEmpleado = ++Empleado.contadorEmpleado;
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
        sb.append(", ").append(super.toString()); 
        sb.append('}');
        return sb.toString();
    }
}
