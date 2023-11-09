
package domain;

public class Persona {

   
    //Cargamos atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    //Constructor
    public Persona(String nombre){
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        Persona.contadorPersona++;//NO utilizar el operador this
        //Vamos a asiganar un nuevo valor a variable idPersona
        this.idPersona = Persona.contadorPersona;
        
    }
     public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
}
