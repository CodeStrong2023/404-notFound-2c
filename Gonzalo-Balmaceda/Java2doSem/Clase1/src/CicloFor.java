public class CicloFor {
    public static void main(String[] args) {

        System.out.println("==== continue ====");
        for (int contador = 0; contador < 7; contador++){
            if (contador % 2 != 0){
                continue; // Si se cumple la condicion del if esta palabra hara que siga iterando el for.
                // y si encuentra un número que dividido por 2 da cero (no se cumple la condicion) lo mostrara en consola.
            }
            System.out.println("numeros pares = " + contador);
        }

        System.out.println("==== break ====");
        for (int contador = 0; contador < 7; contador++){
            if (contador % 2 == 0){
                System.out.println("contador = " + contador);
                break; // Esta palabra rompe con el ciclo.
            }
        }
    }
}
