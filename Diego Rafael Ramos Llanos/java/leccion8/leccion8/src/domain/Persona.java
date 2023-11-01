
package domain;

public class Persona {
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    //constructor
    public Persona(String nombre){
        this.nombre=nombre;
        //incrementar el contador por cada objeto nuevo
        Persona.contadorPersona++; //no utilizar el operador this
        //Vamos a asignar un nuevo valor a la variable idPErsona
        this.idPersona=Persona.contadorPersona;
    }
//    public static int getContadorPersona() {
//        return contadorPersona;
//    }
//
//    public static void setContadorPersona(int aContadorPersona) {
//        contadorPersona = aContadorPersona;
//    }    

    public int getIdPersona() {
        return idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
}
