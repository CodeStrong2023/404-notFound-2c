package domain;

public class Empleado extends Persona{
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;//es para incrementar
    //constructor
    public Empleado(){
        this.idEmpleado=++Empleado.contadorEmpleados;
    }
    public Empleado(String nombre,double sueldo){
        //super(nombre);
        this();//estamos llamando desde aqui al constructor vacio
        this.nombre=nombre;
        this.sueldo=sueldo;
    }

    public int getIdEmpleado() {
        return idEmpleado;
    }

    public void setIdEmpleado(int idEmpleado) {
        this.idEmpleado = idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(',').append(super.toString());
        sb.append("}");
        return sb.toString();
    }
    
}
