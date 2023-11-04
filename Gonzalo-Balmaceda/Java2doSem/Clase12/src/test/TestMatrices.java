package test;

import domain.Persona;

import java.util.Objects;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);

        // Fila 1
        edades[0][0] = 5; // Llenado manual. (Columna 1)
        edades[0][1] = 6; // Es una columna diferente. (Columna 2)
        // Fila 2
        edades[1][0] = 7;
        edades[1][1] = 8;
        // Fila 3
        edades[2][0] = 9;
        edades[2][1] = 10;

        System.out.println("edades 0-0 = " + edades[0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("edades 2-0 = " + edades[2][0]);
        System.out.println("edades 2-1 = " + edades[2][1]);

        // Recorremos la matriz.
        System.out.println("\nRecorremos la matriz con el ciclo 'for'");
        for (int fila = 0; fila < edades.length; fila++) {
            for (int colum = 0; colum < edades[fila].length; colum++) {
                System.out.println("edades " + fila + "-" + colum + " = " + edades[fila][colum]);
            }
        }

        // Sintaxis Clasica.
        //String frutras[][] = new String[3][2];

        // Sintaxis Simplificada.

        String frutas[][] = {{"Limón", "Pomelo"}, {"Ciruela", "Kiwi"}, {"Banana", "Manzana"}};

        System.out.println("\nSintaxis simplificada");
        imprimir(frutas);

//        for (int i = 0; i < frutas.length; i++) {
//            for (int j = 0; j < frutas[i].length; j++) {
//                System.out.println("frutas " + i + "-" + j + " = " + frutas[i][j]);
//            }
//        }

        // Creamos una matriz de objetos.
        Persona persona[][] = new Persona[3][2];

        persona[0][0] = new Persona("Gonzalo");
        persona[0][1] = new Persona("Luciano");

        persona[1][0] = new Persona("Claudia");
        persona[1][1] = new Persona("Mirta");

        persona[2][0] = new Persona("Dario");
        persona[2][1] = new Persona("Agustin");

        System.out.println("\nMatriz de objetos");
        imprimir(persona);
    }

    // Método para imprimr la matriz.
    public static void imprimir(Object matriz[][]) {
            for (int i = 0; i < matriz.length; i++) {
                for (int j = 0; j < matriz[i].length; j++) {
                    System.out.println("matriz " + i + "-" + j + " = " + matriz[i][j]);
                }
            }
    }

}
