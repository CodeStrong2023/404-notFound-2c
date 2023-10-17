package dominio;

public class Persona {
    // Atributos
    private String nombre; 
    private double sueldo;
    private boolean eliminado;
    
    // Constructor (Debe llevar el mismo nombre que la clase)
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }

    public String getNombre() { // GETTER: OBTIENE INFORMACIÓN DEL ATRIBUTO. (MÉTODOS DE ACCESO)
        return nombre;
    }

    public void setNombre(String nombre) { // SETTER: MODIFICA EL VALOR DEL ATRIBUTO. (MÉTODOS DE ACCESO)
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() { // En un tipo boolean en vez de utilizar el GET, se utiliza la palabra IS por qué un boolean es una pregunta de V o F. (¿IS - Está eliminado?)
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    public String toString(){ // Convierte e una cadena cada atributo
        return "Persona [ nombre: "+this.nombre+
                ", sueldo: "+this.sueldo+
                ", eliminado: "+this.eliminado+" ]";
    }
    
}
