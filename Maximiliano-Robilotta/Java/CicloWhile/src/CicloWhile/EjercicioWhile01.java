package CicloWhile;
// Cuando trabajamos con ciclos debemos revisar una condición
// Si la condición es verdadera se ejecuta una sentencia o pueden ser varias
// Y regresa a ser la misma condición, mientras siga siendo verdadera
// Va a volver a ejecutarla hasta que la concición cambia a falso
// Y termina la repetición del ciclo. (Definicion o fundamento de ciclo)

public class EjercicioWhile01 {

    public static void main(String[] args) {
        var conteo = 0; // Inferencia de tipos
        while (conteo <= 7) {
            System.out.println("conteo = " + conteo);
            conteo++; // Vamos aumentando en 1 la variable.
        }

        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador <= 7);
        
        
// Ciclo for en JAVA: Maneja un número determinado de iteraciones, tiene una 
// condición que se debe revisar, si es verdadera se ejecuta el código dentro del
// ciclo, si es falsa no se ejecuta. Cuando la condición se cumple este 
// comienza un incremento o decremento hasta que la condición sea falsa y salga.
      
        for(var contando = 0; contando <= 7; contando++){ 
            // El primer espacio entre los punto y coma es para declarar una variables
            // de tipo contador o iterador, la cuál se incrementa.
            //El segundo espacio es para la condición a cumplir.
            //El tercer espacio es para incrementar o decrementar el iterador, contador o variable.
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break; // Cuando se cumple la condición break rompe el ciclo y sale.
            }
            
        }
        
        for(var contando = 0; contando <= 7; contando++){
            if(contando % 2 != 0){
                continue; // Vamos a la siguiente iteración, continua avanzando en el ciclo.
            }
            System.out.println("contando = " + contando);
            
        }
        
        // Etiquetas Labels: Una etiqueta permite indicar a las palabras continue y break
        // ir hacia un lugar específico en el programa, las etiquetas se combinan con las palabras continue o break.
        inicio:
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio;
            } 

        }
    }
}
