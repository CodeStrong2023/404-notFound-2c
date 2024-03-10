/*
Ejercicio 7: Crear una matriz "marco" de tamaño 5x5: todos sus elementos
deben ser 0 salvo los de los bordes que deben ser 1. Mostrarla.
 */
package ejerciciosde2docuatrimvacaciones;

public class ejerc9 {

    public static void main(String[] args) {
        int[][] marco = new int[5][5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (i == 0 || i == 4 || j == 0 || j == 4) {
                    marco[i][j] = 1;
                } else {
                    marco[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(marco[i][j] + " ");
            }
            System.out.println();
        }
    }
}
