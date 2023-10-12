package domain;

import java.util.Date;

public class Cliente extends Persona{

    public static int getContadorCliente() {
        return contadorCliente;
    }

    public static void setContadorCliente(int aContadorCliente) {
        contadorCliente = aContadorCliente;
    }

    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{idCliente=").append(idCliente);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }

    
    //atributos
    private int idCliente;
    private Date fechaRegistro;//importar la clase Date
    private boolean vip; //very important person
    private static int contadorCliente;//tipo estatico
    
    //constructor
    public Cliente(Date fechaRegistro,boolean vip,String nombre,char genero,int edad,String direccion){
        super(nombre,genero,edad,direccion);
        this.idCliente=++Cliente.contadorCliente;
        this.fechaRegistro=fechaRegistro;
        this.vip=vip;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public Date getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}
