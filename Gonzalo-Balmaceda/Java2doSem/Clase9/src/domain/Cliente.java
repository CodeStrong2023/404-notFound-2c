package domain;

import java.util.Date;

public class Cliente extends Persona {
    // El modificar de acceso va a hacer privado, ya que esta clase no se heredara a nadie.
    private int idCliente;
    private static int contadorCliente; // Aumente el idCliente.
    private Date fechaRegistro;
    private boolean vip;

    // Constructor.
    public Cliente(Date fechaRegistro, boolean vip, String nombre, char genero, int edad, String direccion) {
        super(nombre, genero, edad, direccion); // Llamamos a todos los argumentos de la clase padre 'Persona'.
        this.idCliente = ++Cliente.contadorCliente;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    // Getters y Setters.
    public int getIdCliente() {
        return this.idCliente;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() { // Al ser booleano utiliza el 'is' y no el 'set', ya que lo toma como una pregunta.
        return vip;
    }

    public void setVip(Boolean vip) {
        this.vip = vip;
    }

    // Utilizamos la clase String building, ya que es más eficiente.
    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Cliente{");
        sb.append("idCliente= ").append(idCliente);
        sb.append(", fechaRegistro= ").append(fechaRegistro);
        sb.append(", vip= ").append(vip);
        sb.append(", ").append(super.toString()); // Llamamos al toString() de la clase padre.
        sb.append('}');
        return sb.toString();
    }
}
