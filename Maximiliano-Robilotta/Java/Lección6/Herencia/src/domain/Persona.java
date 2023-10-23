package domain;

public class Persona {
    /* Los atributos private que son para el encapsulamiento no se hereda a las clases hijas
    Si queremos que las clases hijas accedan se utiliza el modificador protected.
    Si no se le asigna nada, el atributo puede se default o package.
    */
    // Atributos de Herencia
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;
    
    // Constructor vacío: este es para crear objetos sin necesidad de inicializar
    // los atributos de la clase
    public Persona(){ // Constructor 1
        
    }
    
    public Persona(String nombre){ // Constructor 2
        this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String direccion) { // Constructor 3 completo que apunta a todos los atributos
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    public String getDireccion() {
        return this.direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

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

//    // El toString va a imprimir el estado de cada objeto con el valor de cada atributo
//    @Override // Reescribe el toString, heredado de la clase padre Object
//    public String toString() {
//        return "Persona{" + "nombre=" + nombre + ", genero=" + genero + ", edad=" + edad + ", direccion=" + direccion + '}';
//    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion=").append(direccion);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
    
    
}
