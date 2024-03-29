package domain;

public class Persona {
    // Atributos de herencia.
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;

    // Constructor vacio: Este es para crear objetos sin necesidad de inicializar
    // los atributos de la clase.

    public Persona() {} // Constructor 1.

    public Persona(String nombre) { // Constructor 2.
       this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String direccion) { // Constructor 3
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    // Getters y Setters.
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getDireccion() {
        return this.direccion;
    }

    // Creamos en toString().

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Persona{");
        sb.append("nombre='").append(nombre).append('\'');
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion='").append(direccion).append('\'');
        sb.append(", ").append(super.toString()); // Nos mostrara la dirección de memoria que esta usando.
        sb.append('}');
        return sb.toString();
    }
}
