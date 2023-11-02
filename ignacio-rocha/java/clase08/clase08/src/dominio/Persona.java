package dominio;

public class Persona {
    //Atributos
    private String nombre;
    private boolean eliminado;
    private double sueldo;
    //constructor
    public Persona(String nombre,double sueldo, boolean eliminado){
        this.nombre=nombre;
        this.sueldo=sueldo;
        this.eliminado=eliminado;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    public String toString(){//convierte en una cadena cada atributo
        return "Persona[nombre: "+this.nombre+", sueldo: "+this.sueldo+", eliminado: "+this.eliminado+" ]";
        
    }
    
    
    
    
    
    
    
}
