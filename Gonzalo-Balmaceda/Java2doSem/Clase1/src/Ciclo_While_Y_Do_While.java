public class Ciclo_While_Y_Do_While {
    public static void main(String[] args) {

        System.out.println("==== Ciclo while ====");
        var conteo = 0;
        while (conteo < 7){ // Mientras que conteo sea menor a 7 aumentara en uno.
            System.out.println("conteo = " + conteo);
            conteo++; // conteo ira incrementando en uno por cada recorrido del while.
        }

        System.out.println("==== Ciclo do/while ====");
        // El ciclo do/while se ejecutará minimo una vez aunque no se cumpla la condicion del while.
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador < 7);
    }
}
