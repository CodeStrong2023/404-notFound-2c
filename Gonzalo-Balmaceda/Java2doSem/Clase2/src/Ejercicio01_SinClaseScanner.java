import javax.swing.*;

public class Ejercicio01_SinClaseScanner {
    public static void main(String[] args) {

        int num;

        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));

        int cuadrado = 0;
        while (num >= 0){
            cuadrado = (int)Math.pow(num, 2);
            System.out.println("El numero " + num + " elevado al cuadrado es " + cuadrado);

            System.out.println("Ingrese otro numero: ");
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero"));
        }
        System.out.println("Programa finalizado por que se ingreso un numero negativo");

    }
}
