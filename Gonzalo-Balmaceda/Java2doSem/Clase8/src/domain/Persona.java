package domain;

public class Persona {
    private int idPersona;
    private static int contadorPersona;
    private String nombre;

    // Constructor.
    public Persona(String nombre) {
        this.nombre = nombre;
        // Incrementar el contador para cada objeto nuevo.
        Persona.contadorPersona++;
        // Vamos a asignar un nuevo valor a la variable idPersona.
        this.idPersona = Persona.contadorPersona;
    }

    public static int getContadorPersona(int contadorPersona) {
        return contadorPersona;
    }

    public static void setContadorPersona(int contadorPersona) {
        contadorPersona = contadorPersona;
    }

    public int getIdPersona(int idPersona) {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre(String nombre) {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override // Agrega información extra al metodo que estamos definiendo.
    public String toString() {
        return "Persona [ idPersona: " + idPersona + ", nombre: " + nombre + " ]";
    }
}
